## DAST (OWASP ZAP) Black-Box Testing Documentation for Django Applications

### 1. Overview

OWASP ZAP is an open-source Dynamic Application Security Testing (DAST) tool used to discover runtime vulnerabilities and security misconfigurations by interacting with a running web application from the outside (Black-Box).
In this guide, we use **ZAP as a proxy**, explore the application manually, then run **Spider + Active Scan**, export results as **JSON**, and finally **unify** them into the project’s **Unified JSON schema**.

---

### 2. Scan Type

We performed the following scan modes:

#### 2.1 Unauthenticated Scan

* Scan without logging in (public pages only).
* Captures vulnerabilities reachable by unauthenticated users.

#### 2.2 Authenticated Scan (user/admin)

* Scan after logging in through the browser while proxied by ZAP.
* Captures vulnerabilities in protected areas based on the authenticated session.

> Note: If an admin role exists, repeat authenticated scan using admin credentials to maximize coverage of admin-only endpoints.

---

### 3. Prerequisites

Ensure the following are available:

* Running Django web application (target example: `http://127.0.0.1:8000`)
* OWASP ZAP installed
* Browser (Chrome/Firefox)
* Optional: ZAP certificate imported (needed if scanning HTTPS through interception)

---

### 4. ZAP Setup as Proxy (Mandatory)

#### 4.1 Start ZAP

* Open OWASP ZAP.

#### 4.2 Configure Browser Proxy

Set your browser proxy to point to ZAP:

* Host: `127.0.0.1`
* Port: `8080` (or the port you configured in ZAP)

#### 4.3 HTTPS Certificate (If Applicable)

If your target is HTTPS and you need to intercept traffic:

* In ZAP: Tools → Options → Network → Server Certificates
* Export and import certificate into the browser trust store.

---

### 5. Execution Steps

#### 5.1 Application Exploration (Manual)

With the browser proxied through ZAP, manually browse key flows, e.g.:

* Home `/`
* Products listing/search `/products/`
* Product details (if applicable)
* Login `/accounts/login/`
* Register `/accounts/register/`
* Cart `/cart/` (if applicable)
* Any API endpoints included in your project scope

✅ Goal: Ensure requests appear in ZAP (Sites tree + History).

---

#### 5.2 Spider (Crawling)

Run Spider on the main target:

* In ZAP: Right click target → Attack → **Spider**
* Wait until spider finishes.

---

#### 5.3 Active Scan (Attack / Fuzzing)

Run Active Scan after spider completes:

* In ZAP: Right click target → Attack → **Active Scan**
* Monitor Alerts tab while scan runs.

---

### 6. Authentication

#### 6.1 Method Used

Authentication was handled using **cookie/session** (typical Django approach).

Examples observed during proxied browsing:

* Session cookie (e.g., `sessionid`)
* CSRF cookie/token (e.g., `csrftoken`)

#### 6.2 How Authenticated Scan Was Achieved

1. Start ZAP proxy
2. Open browser with proxy enabled
3. Log in as user/admin normally via the application login page
4. Confirm authenticated requests appear in ZAP History
5. Run Spider + Active Scan again while authenticated

---

### 7. Exporting Results as JSON (Required)

#### 7.1 Export Raw ZAP Results (JSON)

Export scan results as JSON from ZAP:

* Reports / Generate Report → choose **JSON** (or export via ZAP API)
* Save output as:
  `data/raw/dast_zap.json` *(name can vary)*

> We also keep HTML/PDF reports for human-readable reporting if needed.

---

### 8. Unified JSON Output (Required)

#### 8.1 Goal

Convert ZAP raw JSON into the unified schema required by the project.

#### 8.2 Output Files

Save unified outputs here:

* `data/unified/dast_unified_clean.json`
  (summary/normalized alerts, counts, metadata)

* `data/unified/dast_unified_findings.json`
  (detailed findings using unified schema objects)

#### 8.3 Unified Finding Object Example

```json
{
  "id": "D-001",
  "name": "Missing Security Headers",
  "location": "GET /",
  "source": "DAST",
  "severity": "Low",
  "risk": 30,
  "evidence": "ZAP alert: Missing Anti-clickjacking Header",
  "explain": "Missing security headers can increase exposure to browser-based attacks.",
  "fix": "Add security headers via Django middleware or reverse proxy.",
  "tags": ["OWASP A05: Security Misconfiguration", "CWE-693"]
}
```

---

### 9. Notes / Limitations

#### 9.1 Endpoints Not Reachable by DAST

DAST can only scan what it can reach via crawling/browsing:

* Admin-only endpoints are not reachable without admin login
* API endpoints not linked in UI may not be discovered automatically
* Some endpoints may be blocked by CSRF or require specific workflow steps

#### 9.2 Scope Control (Important)

To avoid scanning external domains (CDNs/third-party services), ensure:

* The active scan scope is limited to your app base URL (e.g., `127.0.0.1:8000`)
* External sites are excluded from scope if they appear in the Sites tree

---

### 10. Deliverables (End of Week)

* `docs/dast_run.md`
* `data/unified/dast_unified_clean.json`
* `data/unified/dast_unified_findings.json`
إذا بدك، ابعثلي **شكل فولدرات مشروعكم الحقيقي** (هل عندكم `data/raw/` ولا لا) وأنا أعدل لك المسارات بالضبط عشان تكون مطابقة 100% للتسليم.
