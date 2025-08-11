<p align="center">
  <img src="https://img.shields.io/badge/status-active-brightgreen.svg"/>
  <img src="https://img.shields.io/badge/platform-linux-blue"/>
  <img src="https://img.shields.io/badge/license-MIT-purple"/>
  <img src="https://img.shields.io/badge/python-3.8+-yellow.svg"/>
</p>

<h1 align="center">🔐 ZIP Password Cracker & Wordlist Generator</h1>

<p align="center">
  <em>Modular Python tool to crack AES-encrypted ZIP files using smart, realistic password generation.</em>
</p>

---

## 📌 Overview

**ZIP Password Cracker & Wordlist Generator** is a modular Python script that attempts to crack encrypted ZIP files using a realistic wordlist generator based on common password patterns.

Ideal for:

- 🔐 Ethical password recovery  
- 🧠 Research in password entropy and attack simulation  
- 🧪 Red team simulations or lab exercises  

---

## ⚙️ Features

- 📁 Decrypts AES-encrypted ZIP files using `pyzipper`
- 🧠 Generates realistic passwords with common patterns and mutations
- 🔄 Simulates human-like mutations (e.g., `admin2023`, `letmein!`, `pass1234`)
- 📊 Calculates simple entropy scores for generated passwords
- 🧪 Designed for ethical usage in CTFs, labs, or offline recovery testing

---

## 🚀 Usage

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/zip-password-cracker.git
cd zip-password-cracker
```

### 2. Run the Script

```bash
python main.py --input_zip secret.zip
```

Optional: use a custom wordlist

```bash
python main.py --input_zip secret.zip --wordlist custom_list.txt
```

---

## 📦 Requirements

- Python 3.8+
- `pyzipper` library

Install dependencies:

```bash
pip install - r requirements.txt
```

---

## ⚠️ Disclaimer

This tool is developed for educational and ethical penetration testing purposes only.  
**Do not use this tool on systems or files you do not have explicit permission to test.**

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**LUCAS**  
🧠 Red Team & Malware Research Enthusiast  
🎓 HTB (Hackthebox student)
🔬 Focused on realistic, anti-mainstream security tooling  
💀 Specialized in offensive security
