OWASP ZAP DAST – Secure Django Application
Overview

OWASP ZAP was used to perform Dynamic Application Security Testing (DAST) on the secure version of a Django web application.
The scan was executed using an automated black-box testing approach, simulating real-world attacks against a running application without access to source code.

Tool Information

Tool: OWASP ZAP

Testing Type: DAST (Black-Box)

Scan Mode: Automated Scan

Target Framework: Django

Scan Scope
Application Type

Secure Django Web Application

Target URL
http://127.0.0.1:8000

Scope Rules

Only application-owned endpoints were included

External domains and third-party services were excluded

Scan scope limited to the base application URL

Security Baseline (Secure Configuration)

The secure version of the application applies OWASP-recommended security controls, including:

Authentication and authorization enforcement

CSRF protection enabled

Secure session and cookie attributes

HTTP security headers configured

Input validation and output encoding

Debug mode disabled

Scan Execution
Scan Type

Unauthenticated Automated Scan

Authenticated Automated Scan (session-based authentication)

Automated Scan Workflow

OWASP ZAP configured as an intercepting proxy

Initial manual interaction to establish application context

Automated Spider Scan for endpoint discovery

Automated Active Scan for vulnerability detection

The automated scan executed attack payloads targeting common web vulnerabilities such as injection flaws, XSS, and security misconfigurations.

Results Summary

No high or critical severity vulnerabilities detected

Only low-risk or informational findings observed

Secure configuration significantly reduced attack surface

Findings mainly related to defensive headers and informational alerts

Output Artifacts
Raw ZAP Output
data/raw/dast_zap_secure.json

Unified JSON Outputs
data/unified/dast_secure_unified_clean.json

Unified JSON Finding Template
[
  {
    "id": "D-SEC-001",
    "name": "Missing Security Header",
    "location": "GET /",
    "source": "DAST",
    "tool": "OWASP ZAP",
    "severity": "Low",
    "risk": 20,
    "evidence": "ZAP alert: X-Frame-Options header not set",
    "explain": "Missing security headers may increase exposure to browser-based attacks such as clickjacking.",
    "fix": "Configure security headers using Django middleware or web server settings.",
    "tags": ["OWASP A05: Security Misconfiguration", "CWE-693"]
  }
]

Notes

DAST testing is limited to reachable endpoints

Secure configuration minimizes true positives

Automated scans complement SAST and AI-based static analysis
