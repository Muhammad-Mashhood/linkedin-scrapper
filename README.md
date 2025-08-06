
# 🚀 LinkedIn Post Reactors & Commenters Scraper

> **Easily extract all users who reacted to or commented on any LinkedIn post.**

---

## ✨ Features

- 🔍 Scrapes all users who **reacted** to a LinkedIn post
- 💬 Scrapes all users who **commented** on the same post
- 📄 Outputs a CSV with: `Name`, `Profile URL`, `Type` (Reaction/Comment)
- 🔒 Uses environment variables for sensitive info
- 🔄 Handles LinkedIn's dynamic loading and scrolling

---

## ⚡ Quick Start

### 1️⃣ Clone the repository
```sh
git clone https://github.com/yourusername/linkedin-scrapper.git
cd linkedin-scrapper
```

### 2️⃣ Install dependencies
Create a virtual environment (recommended):
```sh
python -m venv .venv
.venv\Scripts\activate  # On Windows
```
Install required packages:
```sh
pip install selenium pandas python-dotenv
```

### 3️⃣ Configure your environment
- Create a `.env` file in the project root:
  ```env
  LINKEDIN_POST_URL=your_linkedin_post_url_here
  COOKIES_FILE=cookies.json
  OUTPUT_CSV=linkedin_reactors.csv
  ```
- Export your LinkedIn cookies as `cookies.json` (use a browser extension like [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg)).
- Make sure `.env` and `cookies.json` are in `.gitignore` (already set up).

### 4️⃣ Download ChromeDriver
- Download the version of ChromeDriver that matches your Chrome browser from [here](https://chromedriver.chromium.org/downloads).
- Place `chromedriver.exe` in your project folder or ensure it's in your PATH.

---

## ▶️ Usage
Run the script:
```sh
python linkedin_post_reactors_scraper.py
```

The script will:
1. Log in to LinkedIn using your cookies
2. Scrape all reactors
3. Scrape all commenters
4. Save the results to the specified CSV file

---

## 🔐 Security & Privacy
- **Never commit your `.env` or `cookies.json` to GitHub!**
- All sensitive info is loaded from environment variables.
- The script is for educational and authorized use only. Scraping LinkedIn may violate their Terms of Service.

---

## ⚠️ Disclaimer
This project is for educational purposes. Use responsibly and at your own risk.

---

**Author:** [Muhammad Mashhood](https://github.com/Muhammad-Mashhood)
