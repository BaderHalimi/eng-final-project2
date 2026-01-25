"""
Accounts Views - SECURE VERSION
عروض الحسابات الآمنة
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetConfirmView,
    PasswordResetDoneView, PasswordResetCompleteView
)
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.core.cache import cache
from django.contrib import messages
from django.conf import settings

from .models import CustomUser, Address, UserActivity
from .forms import (
    SecureRegistrationForm, SecureLoginForm, 
    SecurePasswordChangeForm, ProfileUpdateForm, AddressForm
)

import logging
import secrets

logger = logging.getLogger(__name__)


def get_client_ip(request):
    """استخراج IP العميل بشكل آمن"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def log_activity(user, activity_type, request, extra_data=None):
    """تسجيل نشاط المستخدم"""
    UserActivity.objects.create(
        user=user,
        activity_type=activity_type,
        ip_address=get_client_ip(request),
        user_agent=request.META.get('HTTP_USER_AGENT', '')[:500],
        extra_data=extra_data or {}
    )


@never_cache
@csrf_protect
@require_http_methods(["GET", "POST"])
def register_view(request):
    """
    تسجيل مستخدم جديد - آمن
    أمان:
    - CSRF protection
    - Rate limiting
    - Input validation
    - Password strength check
    """
    # Rate limiting - 5 محاولات تسجيل في الساعة
    ip = get_client_ip(request)
    cache_key = f"register_attempts_{ip}"
    attempts = cache.get(cache_key, 0)
    
    if attempts >= 5:
        messages.error(request, 'تم تجاوز عدد محاولات التسجيل. يرجى المحاولة لاحقاً.')
        return redirect('accounts:login')
    
    if request.method == 'POST':
        form = SecureRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            
            # إنشاء رمز التحقق من البريد
            user.generate_email_verification_token()
            
            # تسجيل النشاط
            log_activity(user, 'login', request)
            
            # تسجيل الدخول تلقائياً (بعد التحقق من البريد في الإنتاج)
            login(request, user)
            
            logger.info(f"New user registered: {user.email}")
            messages.success(request, 'تم إنشاء حسابك بنجاح!')
            
            return redirect('products:product_list')
        else:
            # زيادة عداد المحاولات
            cache.set(cache_key, attempts + 1, 3600)
    else:
        form = SecureRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


@never_cache
@csrf_protect
@require_http_methods(["GET", "POST"])
def login_view(request):
    """
    تسجيل الدخول - آمن
    أمان:
    - CSRF protection
    - Account lockout after failed attempts
    - Secure session handling
    - Activity logging
    """
    if request.user.is_authenticated:
        return redirect('products:product_list')
    
    ip = get_client_ip(request)
    
    # Rate limiting على مستوى IP
    ip_cache_key = f"login_attempts_ip_{ip}"
    ip_attempts = cache.get(ip_cache_key, 0)
    
    if ip_attempts >= 10:
        messages.error(request, 'تم تجاوز عدد المحاولات. يرجى المحاولة بعد 30 دقيقة.')
        return render(request, 'accounts/login.html', {'form': SecureLoginForm()})
    
    if request.method == 'POST':
        form = SecureLoginForm(request, data=request.POST)
        email = request.POST.get('username', '').lower()
        
        # التحقق من قفل الحساب
        try:
            user = CustomUser.objects.get(email=email)
            if user.is_locked_out():
                messages.error(request, 'الحساب مقفل مؤقتاً. يرجى المحاولة لاحقاً.')
                log_activity(user, 'failed_login', request, {'reason': 'account_locked'})
                return render(request, 'accounts/login.html', {'form': form})
        except CustomUser.DoesNotExist:
            user = None
        
        if form.is_valid():
            user = form.get_user()
            
            # إعادة تعيين محاولات الفشل
            user.reset_failed_logins()
            user.last_login_ip = ip
            user.save(update_fields=['last_login_ip'])
            
            # تسجيل الدخول
            login(request, user)
            
            # إعدادات الجلسة
            if not form.cleaned_data.get('remember_me'):
                request.session.set_expiry(0)  # تنتهي عند إغلاق المتصفح
            else:
                request.session.set_expiry(1209600)  # أسبوعين
            
            # تدوير معرف الجلسة للحماية من Session Fixation
            request.session.cycle_key()
            
            # تسجيل النشاط
            log_activity(user, 'login', request)
            
            logger.info(f"User logged in: {user.email} from {ip}")
            
            # إعادة التوجيه الآمنة
            next_url = request.GET.get('next', '')
            if next_url and next_url.startswith('/'):
                return redirect(next_url)
            return redirect('products:product_list')
        else:
            # تسجيل محاولة فاشلة
            cache.set(ip_cache_key, ip_attempts + 1, 1800)  # 30 دقيقة
            
            if user:
                user.record_failed_login()
                log_activity(user, 'failed_login', request, {'reason': 'invalid_password'})
            else:
                # تسجيل محاولة بإيميل غير موجود (بدون كشف ذلك)
                UserActivity.objects.create(
                    user=None,
                    activity_type='failed_login',
                    ip_address=ip,
                    user_agent=request.META.get('HTTP_USER_AGENT', '')[:500],
                    extra_data={'email': email, 'reason': 'user_not_found'}
                )
            
            # رسالة عامة لا تكشف ما إذا كان الإيميل موجوداً
            messages.error(request, 'البريد الإلكتروني أو كلمة المرور غير صحيحة')
    else:
        form = SecureLoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})


@login_required
@require_http_methods(["POST"])
@csrf_protect
def logout_view(request):
    """
    تسجيل الخروج - آمن
    """
    log_activity(request.user, 'logout', request)
    logout(request)
    messages.success(request, 'تم تسجيل الخروج بنجاح')
    return redirect('accounts:login')


@login_required
@csrf_protect
@require_http_methods(["GET", "POST"])
def profile_view(request):
    """عرض وتعديل الملف الشخصي"""
    from orders.models import Order
    from cart.models import Wishlist
    from django.db.models import Sum
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            log_activity(request.user, 'profile_update', request)
            messages.success(request, 'تم تحديث الملف الشخصي')
            return redirect('accounts:profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    
    # إحصائيات المستخدم
    orders = Order.objects.filter(user=request.user)
    orders_count = orders.count()
    completed_orders = orders.filter(status='delivered').count()
    total_spent = orders.filter(status='delivered').aggregate(total=Sum('total'))['total'] or 0
    
    # المفضلة
    wishlist_count = Wishlist.objects.filter(user=request.user).count()
    
    # آخر الطلبات
    recent_orders = orders.order_by('-created_at')[:5]
    
    # العنوان الافتراضي
    default_address = request.user.addresses.filter(is_default=True).first()
    if not default_address:
        default_address = request.user.addresses.first()
    
    addresses = request.user.addresses.all()
    activities = request.user.activities.all()[:10]
    
    return render(request, 'accounts/profile.html', {
        'form': form,
        'addresses': addresses,
        'activities': activities,
        'orders_count': orders_count,
        'completed_orders': completed_orders,
        'total_spent': total_spent,
        'wishlist_count': wishlist_count,
        'recent_orders': recent_orders,
        'default_address': default_address,
    })


@login_required
@csrf_protect
@require_http_methods(["GET", "POST"])
def change_password_view(request):
    """
    تغيير كلمة المرور - آمن
    """
    if request.method == 'POST':
        form = SecurePasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            user.password_changed_at = timezone.now()
            user.save(update_fields=['password_changed_at'])
            
            # تحديث الجلسة
            update_session_auth_hash(request, user)
            
            log_activity(user, 'password_change', request)
            messages.success(request, 'تم تغيير كلمة المرور بنجاح')
            
            logger.info(f"Password changed for user: {user.email}")
            
            return redirect('accounts:profile')
    else:
        form = SecurePasswordChangeForm(request.user)
    
    return render(request, 'accounts/change_password.html', {'form': form})


@login_required
@csrf_protect
@require_http_methods(["GET", "POST"])
def add_address_view(request):
    """إضافة عنوان جديد"""
    if request.method == 'POST':
        form = AddressForm(request.POST)
        address_type = request.POST.get('address_type', 'shipping')
        is_default = request.POST.get('is_default') == 'on'
        
        if form.is_valid():
            # إذا كان العنوان الافتراضي، أزل الافتراضي من العناوين الأخرى
            if is_default:
                Address.objects.filter(user=request.user, is_default=True).update(is_default=False)
            
            Address.objects.create(
                user=request.user,
                address_type=address_type,
                is_default=is_default,
                **form.cleaned_data
            )
            messages.success(request, 'تم إضافة العنوان')
            return redirect('accounts:addresses')
    else:
        form = AddressForm()
    
    return render(request, 'accounts/add_address.html', {'form': form})


@login_required
@csrf_protect
@require_http_methods(["GET"])
def addresses_view(request):
    """عرض جميع العناوين"""
    addresses = request.user.addresses.all().order_by('-is_default', '-created_at')
    return render(request, 'accounts/addresses.html', {'addresses': addresses})


@login_required
@csrf_protect
@require_http_methods(["GET", "POST"])
def edit_profile_view(request):
    """تعديل الملف الشخصي"""
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            log_activity(request.user, 'profile_update', request)
            messages.success(request, 'تم تحديث الملف الشخصي')
            return redirect('accounts:profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    
    return render(request, 'accounts/edit_profile.html', {'form': form})


@login_required
@csrf_protect
@require_http_methods(["POST"])
def set_default_address_view(request, address_id):
    """تعيين عنوان كافتراضي"""
    address = get_object_or_404(Address, id=address_id, user=request.user)
    
    # إزالة الافتراضي من العناوين الأخرى
    Address.objects.filter(user=request.user, is_default=True).update(is_default=False)
    
    # تعيين هذا العنوان كافتراضي
    address.is_default = True
    address.save()
    
    messages.success(request, 'تم تعيين العنوان كافتراضي')
    return redirect('accounts:addresses')


@login_required
@csrf_protect
@require_http_methods(["POST"])
def delete_address_view(request, address_id):
    """حذف عنوان"""
    # أمان: التأكد من أن العنوان للمستخدم الحالي
    address = get_object_or_404(Address, id=address_id, user=request.user)
    address.delete()
    messages.success(request, 'تم حذف العنوان')
    return redirect('accounts:profile')


# Password Reset Views with security enhancements
class SecurePasswordResetView(PasswordResetView):
    """
    إعادة تعيين كلمة المرور - آمن
    """
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    
    def form_valid(self, form):
        # Rate limiting
        ip = get_client_ip(self.request)
        cache_key = f"password_reset_{ip}"
        attempts = cache.get(cache_key, 0)
        
        if attempts >= 3:
            messages.error(self.request, 'تم تجاوز عدد المحاولات. يرجى المحاولة لاحقاً.')
            return redirect('accounts:password_reset')
        
        cache.set(cache_key, attempts + 1, 3600)
        
        return super().form_valid(form)


class SecurePasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')
