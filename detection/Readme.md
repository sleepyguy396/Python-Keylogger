# Python Keylogger Detector

A simple, lightweight Python security tool designed to monitor running system processes and flag suspicious activities commonly associated with keyloggers (e.g., unauthorized keyboard hooks, hidden processes, and unverified background tasks).

---

## 📌 Features

* **Process Monitoring:** Scans running background processes against known keylogger behavior patterns.
* **Keyboard Hook Detection:** Checks for active, unauthorized API calls listening to keyboard events.
* **Suspicious DLL/Module Scanning:** Identifies loaded modules commonly leveraged by low-level keyloggers.
* **Logging & Alerting:** Generates real-time console alerts and logs flagged activities to a local file.

---

## 🛠️ Requirements

* **Python:** `3.8+`
* **Operating System:** Windows (Recommended for API hook checks) or Linux/macOS (Process checking only).
* **Dependencies:**
  * `psutil` – Process and system utility monitoring

---
**This software is developed strictly for educational and defensive security research purposes.**

**Authorized Testing Only: You must obtain explicit permission from the device owner before executing this software on any system.**

**Liability: The author assumes no responsibility or liability for unauthorized usage, misuse, or damage caused by this software.**
