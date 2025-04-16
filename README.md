# 🛡️ PORT-SCANNER 🔭 | LIVE Network Security Recon Tool (MacOS)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue.svg" alt="Python 3.13">
  <img src="https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey" alt="Platform">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status">
  <img src="https://img.shields.io/badge/Security-Hardened-critical" alt="Security">
</p>

<p align="center">
  ⚔️ Monitor network activity, detect scans, and identify threats in real-time with AI-ready scanning modules and next-gen integrations!
</p>

---

## 🎬 Demo Preview

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWxjNnU5eTN5emZzd3kxd3FtbXFzZmJmY3BiaWF0emJna3JybThwNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/XaQzXJym8lREI/giphy.gif" width="75%" alt="Live Threat Monitoring">
  <br/>
  <em>Live Threat Monitoring in Action</em>
</p>

---

## 🚀 Project Overview

`PORT-SCANNER` is a live network security monitoring and recon tool designed for MacOS (and beyond 🧠), combining powerful tools like:

- 🛰️ `nmap`
- 🧠 `shodan`
- 📊 CSV & PDF Report Gen
- 🖼️ GUI + CLI scanner interface
- 🧪 Smart detection scripts

Perfect for:
- 👨‍💻 Ethical Hackers
- 🛡️ Cybersecurity Students
- 🔍 Red/Blue Teams

---

## ⚙️ Core Features

| 🔥 Feature                    | 🧠 Description                                                                 |
|------------------------------|------------------------------------------------------------------------------|
| 🎯 Real-Time Monitoring       | Detect live scans, probes, and suspicious port activity                       |
| 🛰️ Shodan Integration         | Pull device info, known vulns, fingerprints from Shodan API                   |
| 🔭 Nmap Scanning              | Use CLI-powered scans with multiple techniques (stealth, version, OS)         |
| 🖥️ GUI Dashboard              | Visual interface to scan, view results, and control options                   |
| 📝 Auto Logging               | Save all activity into logs + formatted CSV/PDF reports                       |
| 🧪 Vulnerability Detection    | Match banner versions against public CVEs                                    |

---

## 🧱 Project Structure

```bash
PORT-SCANNER/
├── auto_scan.py           # Background scan runner
├── gui.py                 # GUI frontend using Tkinter
├── main.py                # Main controller file
├── shodan_scan.py         # Shodan integration module
├── scanner/               # Core nmap-based scan logic
├── integrations/          # Third-party API integrations
├── reports/               # Auto-generated reports
├── utils/                 # Helper scripts
├── wireless/              # Wireless network scan modules
└── requirements.txt       # All dependencies
```

---

## 🛠️ Built With

- 🐍 Python 3.13  
- 🛰️ [Nmap](https://nmap.org/) – Scan engine  
- 🌐 [Shodan](https://shodan.io/) – Internet intelligence  
- 📦 Libraries:
  - `shodan`, `nmap`, `tkinter`, `fpdf`, `pandas`

---

## 📸 Screenshots

> Replace the links with your screenshots!

| GUI Dashboard View | Shodan Scan Result | CSV Report |
|-------------------|--------------------|------------|
| ![](assets/gui-view.png) | ![](assets/shodan-view.png) | ![](assets/csv-report.png) |

---

## ⚡ Usage Instructions

```bash
# 1. (Optional) Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Navigate to project
cd PORT-SCANNER

# 3. Install all dependencies
pip install -r requirements.txt

# 4. Launch CLI Mode
python main.py

# OR launch GUI Mode
python gui.py
```

---

## 📊 Example Output (CLI)

```bash
[INFO] Starting scan on 192.168.0.1...
[SCAN] Detected open ports: 22, 80, 443
[SHODAN] Apache httpd 2.4.7 | CVE-2022-23943 found!
[LOG] Event recorded in /reports/log_2025_04_16.csv
```

---

## 🔁 Roadmap

- [x] GUI Integration
- [x] PDF Report Generation
- [x] Shodan Intelligence Feed
- [ ] 🔐 Firewall Bypass Module (Stealth Scans)
- [ ] 📡 Wireless Device Fingerprinter
- [ ] 🎯 CVE Exploit Validator
- [ ] ⚙️ Plugin System for 3rd-party tools

---

## 📬 Contribute Like a Pro

```bash
# Fork & clone the repo
git clone https://github.com/morningstarxcdcode/PORT-SCANNER.git

# Create a feature branch
git checkout -b feature/awesome-upgrade

# Push your changes
git add .
git commit -m "Add awesome feature"
git push origin feature/awesome-upgrade

# Create a Pull Request and level up!
```

---

## 📦 License

This project is licensed under the [MIT License](LICENSE)

---

## 🤝 Acknowledgements

- `nmap` – Network scanning engine  
- `shodan` – Global device search engine  
- Python community – For keeping security open-source and 🔥  
- You – For using and improving this project!

---

<p align="center">
  <b>🧠 Scan Smarter. Recon Deeper. Learn Ethically.</b><br/>
  <img src="https://readme-typing-svg.herokuapp.com?center=true&width=460&lines=Built+for+Cyber+Explorers;Built+for+Real-Time+Intel;Open+Source+and+Modular" alt="Typing SVG" />
</p>

---

## 🏅 GitHub Badges & Stats

![Repo Size](https://img.shields.io/github/repo-size/morningstarxcdcode/PORT-SCANNER?color=orange&style=for-the-badge)
![Languages](https://img.shields.io/github/languages/count/morningstarxcdcode/PORT-SCANNER?style=for-the-badge)
![Top Language](https://img.shields.io/github/languages/top/morningstarxcdcode/PORT-SCANNER?color=yellow&style=for-the-badge)
![Contributors](https://img.shields.io/github/contributors/morningstarxcdcode/PORT-SCANNER?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/morningstarxcdcode/PORT-SCANNER?style=for-the-badge&color=blue)

### 📊 GitHub Activity Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=morningstarxcdcode&show_icons=true&theme=tokyonight&hide_border=true&custom_title=🚀%20Dev%20Stats)
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=morningstarxcdcode&layout=compact&theme=tokyonight)

---

## 🖼️ Screenshots & Live Demos

### 🎞️ GUI in Action
> A quick look at the user-friendly graphical interface built with Python!

![GUI Demo](https://github.com/morningstarxcdcode/PORT-SCANNER/assets/YOUR_USERNAME/YOUR_IMAGE_ID)

---

### 🛰️ Live Network Scan Detection
> Real-time scanning detection using `nmap` and Shodan API!

![Live Scanner Demo](https://github.com/morningstarxcdcode/PORT-SCANNER/assets/YOUR_USERNAME/YOUR_IMAGE_ID)

---

### 📁 Auto Logs + Threat Reports
> Here’s how auto logs get saved and threats are reported!

![Log Report Example](https://github.com/morningstarxcdcode/PORT-SCANNER/assets/YOUR_USERNAME/YOUR_IMAGE_ID)

---
