# Security Policy

## 🔒 Supported Versions

Security updates are provided for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | ✅ Yes             |
| < 1.0   | ❌ No              |

---

## 🚨 Reporting a Vulnerability

If you discover a security vulnerability in pyDefine, please report it responsibly:

### 📧 Contact

**Email:** yahyabuilds@gmail.com

**Subject:** `[SECURITY] pyDefine Vulnerability Report`

### 📋 What to Include

1. **Description:** Clear description of the vulnerability
2. **Impact:** What can be exploited and potential damage
3. **Reproduction:** Step-by-step instructions to reproduce
4. **Environment:** Python version, OS, pyDefine version
5. **Proof of Concept:** Code or commands demonstrating the issue
6. **Suggested Fix:** If you have one (optional)

### ⏱️ Response Timeline

- **Initial Response:** Within 48 hours
- **Status Update:** Within 7 days
- **Fix Timeline:** Depends on severity (see below)

---

## 🎯 Severity Levels

### 🔴 Critical (Fix within 24-48 hours)
- Remote code execution
- Privilege escalation
- Data exposure affecting all users

### 🟠 High (Fix within 1 week)
- Local code execution
- Denial of service
- Data corruption

### 🟡 Medium (Fix within 2-4 weeks)
- Information disclosure
- Security misconfiguration
- Limited privilege escalation

### 🟢 Low (Fix in next release)
- Minor information leaks
- Theoretical vulnerabilities
- Best practice violations

---

## ⚠️ Known Security Considerations

### `safe_run()` Function

The `safe_run()` function uses Python's `exec()` which can be dangerous:

**⚠️ WARNING:** Only use `safe_run()` with **trusted code** or in **sandboxed environments**.

**Security measures implemented:**
- Restricted `__builtins__` by default
- No file system access by default
- No network access by default
- No dangerous functions (eval, exec, __import__, open)

**Do NOT use for:**
- Running untrusted user code in production
- Processing arbitrary code from the internet
- Executing code without proper validation

**Safe usage:**


✅ Good - trusted code
result = safe_run("print('Hello')")

❌ Bad - untrusted user input
user_code = request.form['code'] # From web form
result = safe_run(user_code) # DANGEROUS!


**Recommended for production:**
- Use containerization (Docker)
- Use proper sandboxing (PyPy sandbox, RestrictedPython)
- Validate and sanitize all inputs
- Run in isolated processes
- Set resource limits (CPU, memory, time)

---

## 🛡️ Security Best Practices

### For Library Users

1. **Keep Updated:** Use the latest version

pip install --upgrade pydefine


2. **Verify Installations:** Check package integrity

pip show pydefine


3. **Use Virtual Environments:** Isolate dependencies

python -m venv venv
source venv/bin/activate
pip install pydefine


4. **Review Code:** Audit code before production use

### For Contributors

1. **No Secrets in Code:** Never commit API keys, passwords, tokens
2. **Validate Inputs:** Check all user inputs
3. **Handle Errors Safely:** Don't expose sensitive information
4. **Use Type Hints:** Help catch type-related bugs
5. **Write Tests:** Include security test cases

---

## 🔍 Security Testing

We perform regular security testing:

- **Static Analysis:** Using Bandit, safety
- **Dependency Scanning:** Automated dependency checks
- **Code Review:** All PRs reviewed for security
- **Fuzzing:** Random input testing
- **Penetration Testing:** Manual security testing

---

## 📜 Disclosure Policy

### Our Commitment

- We will acknowledge receipt within 48 hours
- We will provide regular updates on progress
- We will credit reporters (unless they prefer anonymity)
- We will notify affected users promptly

### Public Disclosure

- **Coordinated Disclosure:** We prefer coordinated disclosure
- **90-Day Window:** Fixes released within 90 days when possible
- **CVE Assignment:** For critical vulnerabilities
- **Security Advisory:** Published after fix is available

---

## 🏆 Hall of Fame

Security researchers who responsibly disclose vulnerabilities will be recognized here:

*No vulnerabilities reported yet*

---

## 📞 Contact

**Security Email:** yahyabuilds@gmail.com  
**PGP Key:** Available upon request  
**GitHub Security:** Use [private vulnerability reporting](https://github.com/mdyahhya/pydefine/security)

---

## 📚 Additional Resources

- [OWASP Python Security](https://owasp.org/www-project-python-security/)
- [Python Security Announcements](https://www.python.org/news/security/)
- [CVE Database](https://cve.mitre.org/)

---

**Thank you for helping keep pyDefine secure! 🔒**

 Powered by pyDefine ● Created by Yahya 
