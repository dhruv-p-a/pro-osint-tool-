# Pro-OSINT Tool 🛡️

A professional multi-platform Open Source Intelligence (OSINT) tool. This project features a modern Android application and a powerful Kali Linux terminal script for deep intelligence gathering.

## 📂 Project Structure

```text
pro-osint-tool/
│
├── android-app/          # Full Android Project (Jetpack Compose)
│   ├── app/              # Source code and UI
│   ├── build.gradle.kts
│   └── settings.gradle.kts
│
├── kali-terminal/        # Python Terminal Edition for Kali Linux
│   ├── osint_tool.py     # Main Python Script
│   └── requirements.txt  # Dependencies
│
├── .gitignore            # Git exclusion rules
├── LICENSE               # MIT License
└── README.md             # Project Documentation
```

## 🚀 Features

-   **Telegram Intelligence:** Scraping public profile data (Name, Bio, Status) directly.
-   **Deep Leak Search:** Simulates searching in massive data breach archives.
-   **Email OSINT:** Identifies if an email is exposed in 500M+ leaked records.
-   **Phone Intel:** Carrier lookup, region identification, and social presence check.
-   **Professional UI:** Modern Android Material 3 design and Kali-style terminal interface.

## 🛠️ Installation & Usage

### Kali Linux Terminal
1. Navigate to the terminal folder:
   `cd kali-terminal`
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run the tool:
   `python3 osint_tool.py`

### Android Application
1. Open the `android-app` folder in **Android Studio**.
2. Build and run on your device or use **Waydroid** in Kali Linux.

---

## ⚖️ Disclaimer
This tool is strictly for **educational and ethical security research**. Use it responsibly.

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request.
