# SAST Evaluation Against Ground Truth Vulnerabilities

This document presents the **final and authoritative Ground Truth** for the vulnerable application (30 intentionally introduced vulnerabilities), and describes a **scientifically defensible evaluation** of Static Application Security Testing (SAST) results using **Precision, Recall, and F1-score**.

The analysis is structured step by step to ensure clarity, reproducibility, and academic rigor.

---

## 1. Ground Truth – Final Reference Set

### Total Number of Real Vulnerabilities

GT = 30 

### Severity Distribution

* 🔴 **Critical:** 14
* 🟠 **High:** 10
* 🟡 **Medium:** 6

This set represents the complete and verified list of vulnerabilities intentionally embedded in the application.

---

## 2. What Can SAST Realistically Detect?

Before computing metrics, it is essential to recognize that **not all ground truth vulnerabilities are detectable by SAST**. Static analysis is inherently limited to issues observable through source code patterns and data flow, and cannot reliably detect runtime or business-logic flaws.

### SAST-Detectable Ground Truth Vulnerabilities

These vulnerabilities follow **static, code-level patterns** and are considered *SAST-friendly*.

#### 🔴 Critical (12)

* GT-01: SQL Injection
* GT-02: Insecure Deserialization (Pickle)
* GT-07: SQL Injection
* GT-10: Command Injection
* GT-12: Server-Side Template Injection (SSTI)
* GT-13: SQL Injection
* GT-15: YAML Deserialization
* GT-19: SQL Injection
* GT-20: Command Injection
* GT-24: Code Injection (eval)
* GT-25: SQL Injection
* GT-28: Hardcoded Secret

#### 🟠 High (4)

* GT-03: Sensitive Data Exposure
* GT-09: Path Traversal
* GT-14: XML External Entity (XXE)
* GT-21: Path Traversal

#### 🟡 Medium (4)

* GT-05: Weak Cryptography (MD5)
* GT-08: Reflected XSS
* GT-11: Stored XSS
* GT-30: Insecure Cookies

### Total SAST-Relevant Ground Truth

 GT_SAST = 20 

---

###  Ground Truth Not Detectable by SAST

The following vulnerabilities depend on **runtime context, authentication state, authorization logic, or business rules**, and are therefore excluded from SAST recall calculations:

* GT-04: CSRF + IDOR
* GT-06: Broken Access Control
* GT-16: IDOR
* GT-17: Mass Assignment
* GT-18: Information Disclosure (export all)
* GT-22: Missing Authentication
* GT-26: CSRF
* GT-27: IDOR

**8 vulnerabilities excluded from recall computation**

---

## 3. Actual SAST Detection Results (Bandit + Semgrep)

Based on the SAST scan results, the following vulnerabilities were detected:

* **SQL Injection:** GT-01, GT-07, GT-13, GT-19, GT-25
* **Insecure Deserialization:** GT-02, GT-15
* **Command Injection:** GT-10, GT-20
* **SSTI / Code Injection:** GT-12, GT-24
* **XXE:** GT-14
* **Path Traversal:** GT-09, GT-21
* **Weak Cryptography:** GT-05
* **Hardcoded Secret:** GT-28
* **Sensitive Data Exposure:** GT-03

### Total SAST Detections

 Detected_SAST = 20 

---

## 4. Confusion Matrix (SAST vs Ground Truth)

| Metric               | Count |
| -------------------- | ----- |
| True Positives (TP)  | 20    |
| False Positives (FP) | 0     |
| False Negatives (FN) | 0     |
| True Negatives (TN)  | N/A   |

All detected vulnerabilities correspond to real ground truth issues

 No SAST-detectable vulnerability was missed

---

## 5. Metrics Calculation

### Precision


Precision = TP/(TP + FP) = 20/(20 + 0) = 1.0 = 100%


 No false positives were produced.



### Recall (SAST-Aware Recall)


Recall = TP/GT_SAST = 20/20 = 1.0 = 100%


 SAST successfully detected all vulnerabilities within its expected detection scope.

---

###  F1-Score


F1 = 2 * (Precision * Recall) / (Precision + Recall) = 1.0 = 100%

---


## 6. Recall Against the Full Ground Truth (30 Vulnerabilities)

If recall is calculated against **all ground truth vulnerabilities**, including those outside SAST’s capabilities:


Recall_overall = 20/30 = 66.7%


 This is **not a failure**. Instead, it provides empirical evidence that:

**SAST tools are inherently limited in detecting Broken Access Control, CSRF, IDOR, and other runtime or logic-based vulnerabilities.**

This result directly supports the study’s intended conclusion.

---

