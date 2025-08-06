# LinkedIn Post Reactors & Commenters Scraper

This Python script uses Selenium to scrape the names and profile URLs of users who reacted to or commented on a specific LinkedIn post. The results are saved in a CSV file.

## Features
- Scrapes all users who reacted to a LinkedIn post
- Scrapes all users who commented on the same post
- Outputs a CSV with columns: Name, Profile URL, Type (Reaction/Comment)
- Uses environment variables for sensitive configuration
- Handles LinkedIn's dynamic loading and scrolling

## Setup

### 1. Clone the repository
```sh
git clone https://github.com/yourusername/linkedin-scrapper.git
cd linkedin-scrapper
```

### 2. Install dependencies
Create a virtual environment (optional but recommended):
```sh
python -m venv .venv
.venv\Scripts\activate  # On Windows
```
Install required packages:
```sh
pip install -r requirements.txt
```
Or manually:
```sh
pip install selenium pandas python-dotenv
```

### 3. Prepare your configuration
- Create a `.env` file in the project root:
  ```env
  LINKEDIN_POST_URL=your_linkedin_post_url_here
  COOKIES_FILE=cookies.json
  OUTPUT_CSV=linkedin_reactors.csv
  ```
- Export your LinkedIn cookies as `cookies.json` (use a browser extension like EditThisCookie).
- Make sure `.env` and `cookies.json` are listed in `.gitignore` (already set up).

### 4. Download ChromeDriver
- Download the version of ChromeDriver that matches your Chrome browser from [here](https://chromedriver.chromium.org/downloads).
- Place the `chromedriver.exe` in your project folder or ensure it's in your PATH.

## Usage
Run the script:
```sh
python linkedin_post_reactors_scraper.py
```

The script will:
1. Log in to LinkedIn using your cookies
2. Scrape all reactors
3. Scrape all commenters
4. Save the results to the specified CSV file

## Security & Privacy
- **Never commit your `.env` or `cookies.json` to GitHub.**
- All sensitive info is loaded from environment variables.
- The script is for educational and authorized use only. Scraping LinkedIn may violate their Terms of Service.

## Disclaimer
This project is for educational purposes. Use responsibly and at your own risk.

---

**Author:** Muhammad Mashhood
