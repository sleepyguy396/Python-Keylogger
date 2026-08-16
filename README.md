# Python-Keylogger
A lightweight, basic Python application designed to demonstrate low-level user input capture using global keyboard listeners. Built for educational purposes, security research, and understanding input logging mechanisms.

---

## 📌 Features

* **Real-Time Input Capture:** Logs keypress events instantly using asynchronous background listening.
* **Special Key Handling:** Properly processes non-character keys (e.g., `Enter`, `Space`, `Backspace`, `Esc`).
* **Clean Exit Condition:** Gracefully terminates execution upon pressing a designated exit key (e.g., `Esc`).
* **Persistent Storage:** Appends captured keystrokes to a local output file (`keylog.txt`).

---

## 🛠️ Requirements

* **Python:** `3.8+`
* **Dependencies:**
  * `pynput` – Library for monitoring and controlling input devices

---
