# جدول النتائج والمقارنات


## 1. AI vs. Ground Truth

| ID Ground Truth | ID AI | اسم الثغرة (Vulnerability Name) | الخطورة (Severity) | الموقع (Location) | الحالة (Status) |
|---|---|---|---|---|---|
| GT-01 | A-006 | SQL Injection in User Search | Critical/High | accounts/views.py | TP |
| GT-02 | A-007 | Insecure Deserialization (Pickle) | Critical/High | accounts/views.py | TP |
| GT-03 | A-008 | Sensitive Data Exposure | High | accounts/views.py | TP |
| GT-04 | A-009 | CSRF + IDOR in Email Update | High | accounts/views.py | TP |
| GT-05 | A-010 | Weak Cryptographic Algorithm (MD5) | Medium | accounts/views.py | TP |
| GT-06 | A-011 | Broken Access Control (Admin) | Critical/High | accounts/views.py | TP |
| GT-07 | A-012 | SQL Injection in Product Search | Critical/High | products/views.py | TP |
| GT-08 | A-013 | Reflected XSS | Medium | products/views.py | TP |
| GT-09 | A-014 | Path Traversal | High | products/views.py | TP |
| GT-10 | A-015 | Command Injection (Report) | Critical/High | products/views.py | TP |
| GT-11 | A-016 | Stored XSS | Medium/High | products/views.py | TP |
| GT-12 | A-017 | Server-Side Template Injection | Critical/High | products/views.py | TP |
| GT-13 | A-018 | SQL Injection in Order Search | Critical/High | orders/views.py | TP |
| GT-14 | A-019 | XXE Injection | High | orders/views.py | TP |
| GT-15 | A-020 | Insecure YAML Deserialization | Critical/High | orders/views.py | TP |
| GT-16 | A-021 | IDOR in Order Invoice | High | orders/views.py | TP |
| GT-17 | A-022 | Mass Assignment | High | orders/views.py | TP |
| GT-18 | A-023 | Information Disclosure | High | orders/views.py | TP |
| GT-19 | A-027 | SQL Injection (Dashboard) | Critical/High | dashboard/views.py | TP |
| GT-20 | A-028 | Command Injection (Backup) | Critical/High | dashboard/views.py | TP |
| GT-21 | A-029 | Path Traversal (Log Reader) | High | dashboard/views.py | TP |
| GT-22 | A-030 | Missing Authentication | Critical/High | dashboard/views.py | TP |
| GT-23 | A-031 | Sensitive Information Disclosure | Critical/High | dashboard/views.py | TP |
| GT-24 | A-032 | Code Injection via eval() | Critical/High | dashboard/views.py | TP |
| GT-25 | A-024 | SQL Injection (Cart Discount) | Critical/High | cart/views.py | TP |
| GT-26 | A-025 | CSRF in Cart Update | Medium/High | cart/views.py | TP |
| GT-27 | A-026 | IDOR in Cart Details | Medium/High | cart/views.py | TP |
| GT-28 | A-002 | Hardcoded Secret Key | Critical/High | mystore/settings.py | TP |
| GT-29 | A-001 | Debug Mode Enabled | High | mystore/settings.py | TP |
| GT-30 | A-004 | Insecure Cookie Configuration | Medium/High | mystore/settings.py | TP |
| N/A | A-003 | Wildcard Allowed Hosts | High | mystore/settings.py | FP |
| N/A | A-005 | Insecure CSRF Cookie | High | mystore/settings.py | FP |

### مقاييس الأداء (Metrics)

| المقياس (Metric) | القيمة (Value) |
|---|---|
| إجمالي اكتشافات AI | 32 |
| إجمالي أهداف Ground Truth | 30 |
| الإيجابيات الحقيقية (TP) | 30 |
| الإيجابيات الخاطئة (FP) | 2 |
| السلبيات الخاطئة (FN) | 0 |
| الدقة (Precision) | 93.75% |
| الاستدعاء (Recall) | 100% |
| درجة (F1-Score) | 96.77% |

**ملاحظة (صيغ المقاييس كما وردت في الملف):**
- Precision =
- Recall =
- F1 = 2 ×

---

## 2. SAST vs. Ground Truth

| ID Ground Truth | ID SAST (المكتشفة) | اسم الثغرة (Vulnerability Name) | الخطورة | الموقع (Location) | الحالة |
|---|---|---|---|---|---|
| GT-01 | S-002, S-019, S-020 | SQL Injection in user search | Critical | accounts/views.py | TP |
| GT-02 | S-001, S-003, S-025 | Insecure Deserialization (Pickle) | Critical | accounts/views.py | TP |
| GT-03 | - | Sensitive Data Exposure - User Info | High | accounts/views.py | FN |
| GT-04 | - | CSRF + IDOR in Email Update | High | accounts/views.py | FN |
| GT-05 | S-004 | Weak Cryptographic Hash (MD5) | Medium | accounts/views.py | TP |
| GT-06 | - | Broken Access Control (Admin) | Critical | accounts/views.py | FN |
| GT-07 | S-017, S-019, S-020 | SQL Injection (Product Search) | Critical | products/views.py | TP |
| GT-08 | - | Reflected XSS | Medium | products/views.py | FN |
| GT-09 | - | Path Traversal (Product Image) | High | products/views.py | FN |
| GT-10 | S-016, S-018, S-021, S-022, S-023 | Command Injection (Report) | Critical | products/views.py | TP |
| GT-11 | - | Stored XSS in Comments | Medium | products/views.py | FN |
| GT-12 | - | Server-Side Template Injection | Critical | products/views.py | FN |
| GT-13 | S-013, S-019, S-020 | SQL Injection (Order Search) | Critical | orders/views.py | TP |
| GT-14 | S-012, S-014 | XXE Injection (XML) | High | orders/views.py | TP |
| GT-15 | S-015 | Insecure YAML Deserialization | Critical | orders/views.py | TP |
| GT-16 | - | IDOR in Order Invoice | High | orders/views.py | FN |
| GT-17 | - | Mass Assignment | High | orders/views.py | FN |
| GT-18 | - | Information Disclosure (Export) | High | orders/views.py | FN |
| GT-19 | S-007, S-019, S-020 | SQL Injection (Dashboard) | Critical | dashboard/views.py | TP |
| GT-20 | S-006, S-009, S-021, S-022, S-023 | Command Injection (Backup) | Critical | dashboard/views.py | TP |
| GT-21 | - | Path Traversal (Log Reader) | High | dashboard/views.py | FN |
| GT-22 | - | Missing Authentication | Critical | dashboard/views.py | FN |
| GT-23 | - | Sensitive Info Disclosure (System) | Critical | dashboard/views.py | FN |
| GT-24 | S-010 | Code Injection via eval() | Critical | dashboard/views.py | TP |
| GT-25 | S-005, S-019, S-020 | SQL Injection (Cart Discount) | Critical | cart/views.py | TP |
| GT-26 | - | CSRF in Cart Update | Medium | cart/views.py | FN |
| GT-27 | - | IDOR in Cart Details | Medium | cart/views.py | FN |
| GT-28 | S-011 | Hardcoded Secret Key | Critical | mystore/settings.py | TP |
| GT-29 | - | Debug Mode Enabled | High | mystore/settings.py | FN |
| GT-30 | - | Insecure Cookie Configuration | Medium | mystore/settings.py | FN |
| N/A | S-008 | Insecure temporary directory | Medium | dashboard/views.py | FP |
| N/A | S-024 | Detected Mailgun API Key | High | mystore/settings.py | FP |

### مقاييس الأداء (Metrics)

| المقياس (Metric) | القيمة (Value) | التوضيح |
|---|---|---|
| إجمالي أهداف GT | 30 | عدد الثغرات في ground truth |
| الإيجابيات الحقيقية (TP) | 13 | عدد الثغرات التي تم رصدها بنجاح |
| السلبيات الخاطئة (FN) | 17 | ثغرات موجودة في ground truth وفشل النظام في رصدها |
| الإيجابيات الخاطئة (FP) | 2 | تنبيهات (S-008, S-024) لم تكن ضمن الـ GT |
| نسبة الاستدعاء (Recall) | 43.33% | تعكس تغطية النظام لـ 13 ثغرة من أصل 30 مطلوبة |
| نسبة الدقة (Precision) | 86.67% | تعكس أن 13 من أصل 15 كانت صحيحة |
| درجة (F1-Score) | 57.78% | التوازن العام |

**ملاحظة (صيغ المقاييس كما وردت في الملف):**
- Precision =
- Recall =
- F1 = 2 ×

---

## 3. Rusalt DAST

| ID GT | ID ZAP | اسم الثغرة (Vulnerability Name) | الخطورة | الموقع المستهدف (URL) | الحالة |
|---|---|---|---|---|---|
| GT-01 | - | SQL Injection in user search | Critical | /accounts/api/users/search/ | FN |
| GT-03 | - | Sensitive Data Exposure | High | /accounts/api/users/debug/ | FN |
| GT-04 | - | CSRF + IDOR in Email Update | High | /accounts/api/users/update-email/ | FN |
| GT-06 | - | Broken Access Control (Admin) | Critical | /accounts/api/admin/action/ | FN |
| GT-07 | - | SQL Injection (Products) | Critical | /api/search/ | FN |
| GT-08 | - | Reflected XSS | Medium | /api/preview/ | FN |
| GT-09 | - | Path Traversal | High | /api/image/ | FN |
| GT-10 | - | Command Injection (Report) | Critical | /api/report/ | FN |
| GT-11 | - | Stored XSS | Medium | /api/comment/ | FN |
| GT-12 | - | SSTI Injection | Critical | /api/render/ | FN |
| GT-13 | - | SQL Injection (Orders) | Critical | /orders/api/search/ | FN |
| GT-14 | - | XXE Injection | High | /orders/api/import/xml/ | FN |
| GT-16 | - | IDOR in Order Invoice | High | /orders/api/invoice/ | FN |
| GT-18 | - | Information Disclosure | High | /orders/api/export/ | FN |
| GT-19 | - | SQL Injection (Dashboard) | Critical | /dashboard/api/search/ | FN |
| GT-20 | - | Command Injection (Backup) | Critical | /dashboard/api/backup/ | FN |
| GT-21 | - | Path Traversal (Logs) | High | /dashboard/api/logs/ | FN |
| GT-22 | - | Missing Authentication | Critical | /dashboard/api/bulk-delete/ | FN |
| GT-23 | - | Sensitive Info Disclosure | Critical | /dashboard/api/system-info/ | FN |
| GT-24 | - | Code Injection (eval) | Critical | /dashboard/api/eval/ | FN |
| GT-25 | - | SQL Injection (Cart) | Critical | /cart/api/discount/ | FN |
| GT-26 | - | CSRF in Cart Update | Medium | /cart/api/update-ajax/ | FN |
| GT-27 | - | IDOR in Cart Details | Medium | /cart/api/details/ | FN |

### مقاييس الأداء (Metrics)

| المقياس (Metric) | القيمة (Value) | التوضيح |
|---|---|---|
| إجمالي أهداف DAST | 23 | عدد الثغرات DAST الموثقة في GT |
| إيجابيات حقيقية (TP) | 0 | لم تنجح الأداة في رصد أي من الثغرات الـ 23 المحددة |
| سلبيات خاطئة (FN) | 23 | فشل النظام في رصد كافة ثغرات الحقن والوصول والمنطق |
| إيجابيات خاطئة (FP) | 15 | عدد الثغرات التي أصدرتها ZAP (مثل HSTS, CSP, Cookies) ولم تكن أهدافاً في GT |
| نسبة الاستدعاء (Recall) | 0% | تغطية صفرية |
| نسبة الدقة (Precision) | 0% | كافة الثغرات الصادرة خارج SCOPE الثغرات الـ 30 الأساسية |
| F1 | 0% | - |

---

## 4. DAST (AI vs. Ground Truth)

| ID Ground Truth | ID AI | اسم الثغرة (Vulnerability Name) | الخطورة (Severity) | الموقع (Location) | الحالة (Status) |
|---|---|---|---|---|---|
| GT-01 | A-006 | SQL Injection in user search | Critical | accounts/views.py | TP |
| GT-03 | A-008 | Sensitive Data Exposure | High | accounts/views.py | TP |
| GT-04 | A-009 | CSRF + IDOR in Email Update | High | accounts/views.py | TP |
| GT-06 | A-011 | Broken Access Control (Admin) | Critical | accounts/views.py | TP |
| GT-07 | A-012 | SQL Injection in Product Search | Critical | products/views.py | TP |
| GT-08 | A-013 | Reflected XSS | Medium | products/views.py | TP |
| GT-09 | A-014 | Path Traversal | High | products/views.py | TP |
| GT-10 | A-015 | Command Injection (Report) | Critical | products/views.py | TP |
| GT-11 | A-016 | Stored XSS | Medium | products/views.py | TP |
| GT-12 | A-017 | SSTI Injection | Critical | products/views.py | TP |
| GT-13 | A-018 | SQL Injection (Order Search) | Critical | orders/views.py | TP |
| GT-14 | A-019 | XXE Injection | High | orders/views.py | TP |
| GT-16 | A-021 | IDOR in Order Invoice | High | orders/views.py | TP |
| GT-18 | A-023 | Information Disclosure | High | orders/views.py | TP |
| GT-19 | A-027 | SQL Injection (Dashboard Search) | Critical | dashboard/views.py | TP |
| GT-20 | A-028 | Command Injection (Backup) | Critical | dashboard/views.py | TP |
| GT-21 | A-029 | Path Traversal (Log Reader) | High | dashboard/views.py | TP |
| GT-22 | A-030 | Missing Authentication | Critical | dashboard/views.py | TP |
| GT-23 | A-031 | Sensitive Information Disclosure | Critical | dashboard/views.py | TP |
| GT-24 | A-032 | Code Injection via eval() | Critical | dashboard/views.py | TP |
| GT-25 | A-024 | SQL Injection (Cart Discount) | Critical | cart/views.py | TP |
| GT-26 | A-025 | CSRF in Cart Update | Medium | cart/views.py | TP |
| GT-27 | A-026 | IDOR in Cart Details | Medium | cart/views.py | TP |

### مقاييس الأداء (Metrics)

| المقياس (Metric) | القيمة (Value) | الملاحظات |
|---|---|---|
| إجمالي أهداف DAST | 23 | بناءً على تصنيف Scope في Ground Truth |
| الإيجابيات الحقيقية (TP) | 23 | تم رصد جميع الثغرات DAST بنجاح |
| الإيجابيات الخاطئة (FP) | 0 | تم استبعاد ثغرات الإعدادات (A-003, A-005) لضمان عدالة المقارنة |
| السلبيات الخاطئة (FN) | 0 | لم يغفل النظام عن أي ثغرة DAST موثقة |
| درجة (F1-Score) | 100% | دقة كاملة في اكتشاف الثغرات القابلة للاستغلال عبر الروابط |

---

## 5. DAST (SAST vs. Ground Truth)

| ID Ground Truth | SAST ID | اسم الثغرة (Vulnerability Name) | الخطورة | الموقع (Location/URL) | الحالة |
|---|---|---|---|---|---|
| GT-01 | S-002, S-019, S-020 | SQL Injection in user search | Critical | /accounts/api/users/search/ | TP |
| GT-03 | - | Sensitive Data Exposure - User Info | High | /accounts/api/users/debug/ | FN |
| GT-04 | - | CSRF + IDOR in Email Update | High | /accounts/api/users/update-email/ | FN |
| GT-06 | - | Broken Access Control (Admin Action) | Critical | /accounts/api/admin/action/ | FN |
| GT-07 | S-017, S-019, S-020 | SQL Injection in Product Search | Critical | /api/search/ | TP |
| GT-08 | - | Reflected XSS in Product Preview | Medium | /api/preview/ | FN |
| GT-09 | - | Path Traversal in Product Image | High | /api/image/ | FN |
| GT-10 | S-016, S-018, S-021, S-022, S-023 | Command Injection (Report Generation) | Critical | /api/report/ | TP |
| GT-11 | - | Stored XSS in Product Comments | Medium | /api/comment/ | FN |
| GT-12 | - | Server-Side Template Injection (SSTI) | Critical | /api/render/ | FN |
| GT-13 | S-013, S-019, S-020 | SQL Injection in Order Search | Critical | /orders/api/search/ | TP |
| GT-14 | S-012, S-014 | XXE - XML External Entity Injection | High | /orders/api/import/xml/ | TP |
| GT-16 | - | IDOR in Order Invoice | High | /orders/api/invoice/ | FN |
| GT-18 | - | Information Disclosure (Export Orders) | High | /orders/api/export/ | FN |
| GT-19 | S-007, S-019, S-020 | SQL Injection in Dashboard Search | Critical | /dashboard/api/search/ | TP |
| GT-20 | S-006, S-009, S-021, S-022, S-023 | Command Injection in Backup | Critical | /dashboard/api/backup/ | TP |
| GT-21 | - | Path Traversal in Log File Reader | High | /dashboard/api/logs/ | FN |
| GT-22 | - | Missing Authentication (Bulk Delete) | Critical | /dashboard/api/bulk-delete/ | FN |
| GT-23 | - | Sensitive Information Disclosure | Critical | /dashboard/api/system-info/ | FN |
| GT-24 | S-010 | Code Injection via eval() | Critical | /dashboard/api/eval/ | TP |
| GT-25 | S-005, S-019, S-020 | SQL Injection in Cart Discount | Critical | /cart/api/discount/ | TP |
| GT-26 | - | CSRF in Cart Update | Medium | /cart/api/update-ajax/ | FN |
| GT-27 | - | IDOR in Cart Details | Medium | /cart/api/details/ | FN |
| N/A | S-008 | Insecure hardcoded temporary directory | Medium | dashboard/views.py | FP |

### مقاييس الأداء (Metrics)

| المقياس (Metric) | القيمة (Value) | الملاحظات |
|---|---|---|
| إجمالي أهداف الحقيقة الأرضية (GT) | 23 | الثغرات المصنفة DAST في Ground Truth |
| الإيجابيات الحقيقية (TP) | 9 | الثغرات التي تم اكتشافها بنجاح (معظمها ثغرات حقن) |
| السلبيات الخاطئة (FN) | 14 | ثغرات موجودة فشل الفحص في رصدها (مثل IDOR وXSS) |
| الإيجابيات الخاطئة (FP) | 1 | تنبيه (S-008) لم يكن ضمن أهداف Ground Truth |
| نسبة الاستدعاء (Recall) | 39.13% | تعكس قدرة الفحص على تغطية 9 ثغرات من أصل 23 |
| نسبة الدقة (Precision) | 90% | تعكس أن 9 من أصل 10 تنبيهات فريدة كانت صحيحة |
| درجة F1 | 54.54% | المتوسط للأداء العام في هذا الاختبار |

**الخلاصة (كما وردت في الملف):** أثبت النظام كفاءة عالية جداً في اكتشاف ثغرات (Injection) القابلة للاستغلال عبر الروابط، لكنه واجه صعوبة كبيرة في رصد ثغرات التحكم في الوصول والمنطق البرمجي في البيئة الديناميكية.

---

## 6. SAST vs. scope "SAST, DAST, AI"

| ID Ground Truth | SAST ID | اسم الثغرة (Vulnerability Name) | الخطورة (Severity) | الموقع (Location) | الحالة (Status) |
|---|---|---|---|---|---|
| GT-01 | S-002, S-019, S-020 | SQL Injection in user search | Critical | /accounts/api/users/search/ | TP |
| GT-03 | - | Sensitive Data Exposure | High | /accounts/api/users/debug/ | FN |
| GT-07 | S-017, S-019, S-020 | SQL Injection in Product Search | Critical | /api/search/ | TP |
| GT-08 | - | Reflected XSS | Medium | /api/preview/ | FN |
| GT-09 | - | Path Traversal (Product Image) | High | /api/image/ | FN |
| GT-10 | S-018, S-021, S-022, S-023 | Command Injection (Report) | Critical | /api/report/ | TP |
| GT-11 | - | Stored XSS in Comments | Medium | /api/comment/ | FN |
| GT-12 | - | SSTI Injection | Critical | /api/render/ | FN |
| GT-13 | S-013, S-019, S-020 | SQL Injection in Order Search | Critical | /orders/api/search/ | TP |
| GT-14 | S-014 | XXE Injection (XML) | High | /orders/api/import/xml/ | TP |
| GT-19 | S-007, S-019, S-020 | SQL Injection (Dashboard) | Critical | /dashboard/api/search/ | TP |
| GT-20 | S-009, S-021, S-022, S-023 | Command Injection (Backup) | Critical | /dashboard/api/backup/ | TP |
| GT-21 | - | Path Traversal (Log Reader) | High | /dashboard/api/logs/ | FN |
| GT-23 | - | Sensitive Information Disclosure | Critical | /dashboard/api/system-info/ | FN |
| GT-24 | S-010 | Code Injection via eval() | Critical | /dashboard/api/eval/ | TP |
| GT-25 | S-005, S-019, S-020 | SQL Injection (Cart Discount) | Critical | /cart/api/discount/ | TP |

### مقاييس الأداء (Metrics)

| المقياس (Metric) | القيمة (Value) | التوضيح |
|---|---|---|
| إجمالي الأهداف | 16 | الثغرات التي تطلب النطاقات الثلاثة معاً [1، 23] |
| إيجابيات حقيقية (TP) | 9 | نجح في اكتشاف كافة ثغرات الحقن (SQL, Command, XXE, Code) |
| سلبيات خاطئة (FN) | 7 | فشل النظام في رصد ثغرات XSS، Path Traversal، SSTI، وتسريب البيانات |
| نسبة الاستدعاء (Recall) | 56.25% | تعكس قدرة النظام على تغطية أكثر من نصف الثغرات المعقدة |
| نسبة الدقة (Precision) | 100% | جميع التنبيهات التي أصدرها النظام لهذا النطاق كانت صحيحة تماماً |
| درجة (F1-Score) | 72% | توازن جيد جداً |
| FP | 2 | - |

---

## 7. Rusalt DAST vs. scope "SAST, DAST, AI"

| معرف GT | ID ZAP | اسم الثغرة (Vulnerability Name) | الخطورة | الحالة |
|---|---|---|---|---|
| GT-01 | - | SQL Injection in user search | Critical | FN |
| GT-03 | - | Sensitive Data Exposure | High | FN |
| GT-07 | - | SQL Injection (Product Search) | Critical | FN |
| GT-08 | - | Reflected XSS | Medium | FN |
| GT-09 | - | Path Traversal (Product Image) | High | FN |
| GT-10 | - | Command Injection (Report) | Critical | FN |
| GT-11 | - | Stored XSS in Comments | Medium | FN |
| GT-12 | - | SSTI Injection | Critical | FN |
| GT-13 | - | SQL Injection (Order Search) | Critical | FN |
| GT-14 | - | XXE Injection (XML) | High | FN |
| GT-19 | - | SQL Injection (Dashboard) | Critical | FN |
| GT-20 | - | Command Injection (Backup) | Critical | FN |
| GT-21 | - | Path Traversal (Log Reader) | High | FN |
| GT-23 | - | Sensitive Information Disclosure | Critical | FN |
| GT-24 | - | Code Injection via eval() | Critical | FN |
| GT-25 | - | SQL Injection (Cart Discount) | Critical | FN |

### مقاييس الأداء (Metrics)

| المقياس (Metric) | القيمة (Value) | التوضيح |
|---|---|---|
| إجمالي أهداف DAST | 16 | عدد الثغرات SAST, DAST, AI الموثقة في GT |
| إيجابيات حقيقية (TP) | 0 | لم تنجح الأداة في رصد أي من الثغرات الـ 23 المحددة |
| سلبيات خاطئة (FN) | 16 | فشل النظام في رصد كافة ثغرات الحقن والوصول والمنطق |
| إيجابيات خاطئة (FP) | 15 | عدد الثغرات التي أصدرتها ZAP (مثل HSTS, CSP, Cookies) ولم تكن أهدافاً في GT |
| نسبة الاستدعاء (Recall) | 0% | تغطية صفرية |
| نسبة الدقة (Precision) | 0% | كافة الثغرات الصادرة خارج SCOPE الثغرات الـ 30 الأساسية |
| F1 | 0% | - |

---

## 8. AI vs. scope "SAST, DAST, AI"

| ID Ground Truth | ID AI | اسم الثغرة (Vulnerability Name) | الخطورة (Severity) | الموقع (Location) | الحالة |
|---|---|---|---|---|---|
| GT-01 | A-006 | SQL Injection in user search | Critical | accounts/views.py | TP |
| GT-03 | A-008 | Sensitive Data Exposure | High | accounts/views.py | TP |
| GT-07 | A-012 | SQL Injection in Product Search | Critical | products/views.py | TP |
| GT-08 | A-013 | Reflected XSS | Medium | products/views.py | TP |
| GT-09 | A-014 | Path Traversal (Product Image) | High | products/views.py | TP |
| GT-10 | A-015 | Command Injection (Report) | Critical | products/views.py | TP |
| GT-11 | A-016 | Stored XSS in Product Comments | Medium | products/views.py | TP |
| GT-12 | A-017 | Server-Side Template Injection | Critical | products/views.py | TP |
| GT-13 | A-018 | SQL Injection in Order Search | Critical | orders/views.py | TP |
| GT-14 | A-019 | XXE Injection (XML) | High | orders/views.py | TP |
| GT-19 | A-027 | SQL Injection (Dashboard) | Critical | dashboard/views.py | TP |
| GT-20 | A-028 | Command Injection (Backup) | Critical | dashboard/views.py | TP |
| GT-21 | A-029 | Path Traversal (Log Reader) | High | dashboard/views.py | TP |
| GT-23 | A-031 | Sensitive Information Disclosure | Critical | dashboard/views.py | TP |
| GT-24 | A-032 | Code Injection via eval() | Critical | dashboard/views.py | TP |
| GT-25 | A-024 | SQL Injection (Cart Discount) | Critical | cart/views.py | TP |

### مقاييس الأداء (Metrics)

| المقياس (Metric) | القيمة (Value) | التوضيح |
|---|---|---|
| إجمالي الأهداف المطلوبة | 16 | الثغرات التي تطلب النطاقات الثلاثة معاً في ملف GT |
| الإيجابيات الحقيقية (TP) | 16 | تم رصد جميع الثغرات الـ 16 بنجاح |
| السلبيات الخاطئة (FN) | 0 | لا توجد أي ثغرة مفقودة ضمن هذا Scope |
| الإيجابيات الخاطئة (FP) | 2 | يصدر النظام 2 تنبيه خاطئ يندرج تحت هذا Scope تحديداً |
| نسبة الاستدعاء (Recall) | 100% | تغطية كاملة وشاملة لكافة الثغرات المستهدفة في هذا النطاق |
| نسبة الدقة (Precision) | 100% | جميع التنبيهات الصادرة لهذا السكوب كانت دقيقة ومطابقة تماماً |
| درجة (F1-Score) | 100% | أداء مثالي يجمع بين التغطية الكاملة والدقة المتناهية |

---

## 9. Final Report

### 9.1 ملخص الإيجابيات الخاطئة (False Positives) حسب الأداة

| Tool | Total Findings (FP) | Precision | Main FP Categories |
|---|---|---|---|
| SAST | 4 | 0 | Integrity Failures, CSRF, XSS, Open Redirect |
| DAST | 25 | 0 | Security Misconfiguration, Information Disclosure, Information Disclosure, Injection |
| AI | 12 | 0 | Context misinterpretation, framework protections, development settings. |

### 9.2 جدول النطاق الكامل (Full Scope GT)

| Tool | Full Scope GT | TP | FP | FN | Precision | Recall | F1 |
|---|---|---|---|---|---|---|---|
| SAST | 30 | 13 | 2 | 17 | 86.67% | 43.33% | 57.78% |
| DAST | 23 | 0 | 15 | 23 | 0% | 0% | 0% |
| AI | 30 | 30 | 2 | 0 | 93.75% | 100% | 96.77% |

### 9.3 جدول النطاق المشترك (Common Scope: SAST + DAST + AI)

| Tool | Full Scope GT | TP | FP | FN | Precision | Recall | F1 |
|---|---|---|---|---|---|---|---|
| SAST | 16 | 9 | 2 | 7 | 81.81% | 56.25% | 66.66% |
| DAST | 16 | 0 | 15 | 16 | 0% | 0% | 0% |
| AI | 16 | 16 | 2 | 0 | 88.9% | 100% | 94.12% |

### 9.4 المقارنة التفصيلية الشاملة (AI vs SAST vs DAST لكل ثغرة)

| ID Ground Truth | اسم الثغرة (Vulnerability Name) | الخطورة (Severity) | الموقع (Location) | AI | SAST | DAST |
|---|---|---|---|---|---|---|
| GT-01 | SQL Injection in User Search | Critical/High | accounts/views.py | ✔ TP | ✔ TP | ✘ FN |
| GT-02 | Insecure Deserialization (Pickle) | Critical/High | accounts/views.py | ✔ TP | ✔ TP | ✘ FN |
| GT-03 | Sensitive Data Exposure | High | accounts/views.py | ✔ TP | ✘ FN | ✘ FN |
| GT-04 | CSRF + IDOR in Email Update | High | accounts/views.py | ✔ TP | ✘ FN | ✘ FN |
| GT-05 | Weak Cryptographic Algorithm (MD5) | Medium | accounts/views.py | ✔ TP | ✔ TP | ✘ FN |
| GT-06 | Broken Access Control (Admin) | Critical/High | accounts/views.py | ✔ TP | ✘ FN | ✘ FN |
| GT-07 | SQL Injection in Product Search | Critical/High | products/views.py | ✔ TP | ✔ TP | ✘ FN |
| GT-08 | Reflected XSS | Medium | products/views.py | ✔ TP | ✘ FN | ✘ FN |
| GT-09 | Path Traversal | High | products/views.py | ✔ TP | ✘ FN | ✘ FN |
| GT-10 | Command Injection (Report) | Critical/High | products/views.py | ✔ TP | ✔ TP | ✘ FN |
| GT-11 | Stored XSS | Medium/High | products/views.py | ✔ TP | ✘ FN | ✘ FN |
| GT-12 | Server-Side Template Injection | Critical/High | products/views.py | ✔ TP | ✘ FN | ✘ FN |
| GT-13 | SQL Injection in Order Search | Critical/High | orders/views.py | ✔ TP | ✔ TP | ✘ FN |
| GT-14 | XXE Injection | High | orders/views.py | ✔ TP | ✔ TP | ✘ FN |
| GT-15 | Insecure YAML Deserialization | Critical/High | orders/views.py | ✔ TP | ✔ TP | ✘ FN |
| GT-16 | IDOR in Order Invoice | High | orders/views.py | ✔ TP | ✘ FN | ✘ FN |
| GT-17 | Mass Assignment | High | orders/views.py | ✔ TP | ✘ FN | ✘ FN |
| GT-18 | Information Disclosure | High | orders/views.py | ✔ TP | ✘ FN | ✘ FN |
| GT-19 | SQL Injection (Dashboard) | Critical/High | dashboard/views.py | ✔ TP | ✔ TP | ✘ FN |
| GT-20 | Command Injection (Backup) | Critical/High | dashboard/views.py | ✔ TP | ✔ TP | ✘ FN |
| GT-21 | Path Traversal (Log Reader) | High | dashboard/views.py | ✔ TP | ✘ FN | ✘ FN |
| GT-22 | Missing Authentication | Critical/High | dashboard/views.py | ✔ TP | ✘ FN | ✘ FN |
| GT-23 | Sensitive Information Disclosure | Critical/High | dashboard/views.py | ✔ TP | ✘ FN | ✘ FN |
| GT-24 | Code Injection via eval() | Critical/High | dashboard/views.py | ✔ TP | ✔ TP | ✘ FN |
| GT-25 | SQL Injection (Cart Discount) | Critical/High | cart/views.py | ✔ TP | ✔ TP | ✘ FN |
| GT-26 | CSRF in Cart Update | Medium/High | cart/views.py | ✔ TP | ✘ FN | ✘ FN |
| GT-27 | IDOR in Cart Details | Medium/High | cart/views.py | ✔ TP | ✘ FN | ✘ FN |
| GT-28 | Hardcoded Secret Key | Critical/High | mystore/settings.py | ✔ TP | ✔ TP | ✘ FN |
| GT-29 | Debug Mode Enabled | High | mystore/settings.py | ✔ TP | ✘ FN | ✘ FN |
| GT-30 | Insecure Cookie Configuration | Medium/High | mystore/settings.py | ✔ TP | ✘ FN | ✘ FN |

### 9.5 أنواع الثغرات المفقودة حسب الأداة (Missed Vulnerability Types)

| Tool | Missed Vulnerability Types | Example GT IDs |
|---|---|---|
| SAST | Sensitive Data Exposure, Broken Access Control (Admin) | GT-03, GT-06 |
| DAST | All | All |
| AI | - | - |

### 9.6 الأسئلة والأجوبة (Questions & Answers)

**أي أداة حققت أعلى Precision في الديمو الضعيف؟**
AI+SAST

**أي أداة حققت أعلى Recall؟**
AI

**أي أداة حققت أفضل F1-score؟**
AI

**أي أداة أنتجت أكبر عدد من False Positives في الديمو الآمن؟**
DAST

**أي أداة كانت الأقل إزعاجاً (False Positives) للمطورين؟**
AI+SAST

**أي أداة كانت الأفضل في كشف ثغرات Injection؟**
SAST+AI

**أي أداة فشلت في كشف Access Control؟**
DAST+SAST

**هل هناك فئة OWASP لا تغطيها إحدى الأدوات؟**
SAST does not cover the following: A01 Broken Access Control, A09 Security Logging and Alerting Failures, A10 Mishandling of Exceptional Conditions

**هل توجد أداة واحدة تغطي جميع أنواع الثغرات؟**
لا توجد أداة بحد ذاتها تغطي جميع أنواع الثغرات

**ما نوع الثغرات التي يفشل فيها SAST عادة؟**
Broken access control, or any error in the app logic that needs strong understanding instead of pattern matching in code.

**ما نوع الثغرات التي يفشل فيها DAST عادة؟**

Business Logic Vulnerabilities (لأنه لا يفهم منطق التطبيق)

Source Code Issues مثل hardcoded secrets أو insecure functions

Authorization flaws غير القابلة للوصول أثناء الـ crawling

Dead / Unreachable code paths

Server-side misconfigurations التي لا تنعكس في HTTP response

لأنه يعتمد على runtime black-box interaction فقط، وليس تحليل الكود أو التدفق الداخلي للتطبيق.

**هل نتائج AI كانت مستقرة أم متغيرة؟**
كانت مستقرة نسبيًا بالنسبة لنسخة الغير أمنة بينما النسخة الأمنة كانت متغيرة

**لو كنت شركة صغيرة، أي أداة تختار أولاً؟ ولماذا؟**
لو شركة صغيرة أو كبيرة الأفضل التكاملية ولكن اذا كنت غير معني بنسبة أمن كبيرة ممكن AI يلبي طلبك

**لو كنت بنك أو نظام حساس، هل تعتمد على أداة واحدة؟**
لا طبعًا لأن كل أداة يوجد بها إيجابيات وسلبيات، والبعض متخصص بالكود المصدري مثل SAST، والآخر عند التشغيل مثل DAST، ولكن معًا بالإضافة لـ AI تحقق نتيجة أفضل، وهيك بكونه مناسب لمثل هيك أعمال، ولكن في مثل هادي الشركات الأفضل أن يكون هناك فريق أمن معلومات مختص للقيام بعملية تحليل أمني يدوي واستخدام الأدوات بشكل صحيح

**ما أفضل استراتيجية أمنية بناءً على النتائج؟**
ليس هناك استراتيجية أفضل من الأخرى، جميعها أصدرت نتائج، ولكن كانت نسبة نتائج AI في اكتشاف الثغرات للمشروع الذي تم خوض التجارب عليه أعلى استراتيجية، ولكن هذا لا يعني أن نعتمد عليه بكل المشاريع لوحده
