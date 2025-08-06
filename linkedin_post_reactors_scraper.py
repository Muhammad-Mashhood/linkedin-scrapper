import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import os
from dotenv import load_dotenv

# --- CONFIGURATION ---
load_dotenv()
LINKEDIN_POST_URL = os.getenv('LINKEDIN_POST_URL')
COOKIES_FILE = os.getenv('COOKIES_FILE', 'cookies.json')
OUTPUT_CSV = os.getenv('OUTPUT_CSV', 'linkedin_reactors.csv')

# --- SETUP SELENIUM ---
options = Options()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)

def load_cookies(driver, cookies_file):
    with open(cookies_file, 'r') as f:
        cookies = json.load(f)
    for cookie in cookies:
        # Fix sameSite for Selenium compatibility
        if 'sameSite' in cookie:
            if cookie['sameSite'] in ['no_restriction', 'unspecified']:
                cookie['sameSite'] = 'None'
        # Remove keys not accepted by Selenium
        for key in ['storeId', 'id', 'hostOnly', 'session']:
            cookie.pop(key, None)
        driver.add_cookie(cookie)

def main():
    driver.get('https://www.linkedin.com')
    time.sleep(3)
    load_cookies(driver, COOKIES_FILE)
    driver.refresh()
    time.sleep(3)
    driver.get(LINKEDIN_POST_URL)
    time.sleep(10)


    # Click on the reactions/likes count to open the list
    try:
        reactions_btn = driver.find_element(By.CSS_SELECTOR, '[aria-label*="reactions"]')
        reactions_btn.click()
        time.sleep(3)
        # Take screenshot for debugging
        driver.save_screenshot('after_reactions_popup.png')
        # Save HTML of the popup for inspection
        with open('reactions_popup.html', 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        print('Screenshot and HTML saved for debugging.')
    except Exception as e:
        print('Could not find reactions button:', e)
        driver.quit()
        return


    # Scroll the popup container to load all users
    try:
        # Find the scrollable container (adjust selector if needed)
        scroll_container = driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__content')
        last_height = driver.execute_script('return arguments[0].scrollHeight', scroll_container)
        for _ in range(30):  # Increase range for more users
            driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight);', scroll_container)
            time.sleep(1.5)
            new_height = driver.execute_script('return arguments[0].scrollHeight', scroll_container)
            if new_height == last_height:
                break
            last_height = new_height
    except Exception as e:
        print('Could not scroll popup container:', e)


    # Scrape user info (Reactions)
    users = []
    user_cards = driver.find_elements(By.CSS_SELECTOR, 'a.link-without-hover-state')
    print(f'Found {len(user_cards)} user cards (reactions).')
    for card in user_cards:
        name = card.text.split('\n')[0]
        profile_url = card.get_attribute('href')
        users.append({'Name': name, 'Profile URL': profile_url, 'Type': 'Reaction'})

    # Go back to the post page to scrape comments
    driver.get(LINKEDIN_POST_URL)
    time.sleep(5)


    # Load all comments by clicking 'Load more comments' buttons
    while True:
        try:
            load_more_btn = driver.find_element(By.CSS_SELECTOR, 'button.comments-comments-list__load-more-comments-button--cr, button[aria-label="Load more comments"]')
            if load_more_btn.is_displayed() and load_more_btn.is_enabled():
                load_more_btn.click()
                time.sleep(2)
            else:
                break
        except Exception:
            break

    # Scrape commenters
    comment_users = []
    # Find all profile links in comments (using the correct class)
    comment_links = driver.find_elements(By.CSS_SELECTOR, 'a.comments-comment-meta__description-container')
    print(f'Found {len(comment_links)} commenter profile links.')
    for a_tag in comment_links:
        name = a_tag.text.strip().split('\n')[0]
        profile_url = a_tag.get_attribute('href')
        if name and profile_url:
            comment_users.append({'Name': name, 'Profile URL': profile_url, 'Type': 'Comment'})

    # Combine and deduplicate by profile URL and type
    all_users = users + comment_users
    seen = set()
    unique_users = []
    for user in all_users:
        key = (user['Profile URL'], user['Type'])
        if key not in seen:
            unique_users.append(user)
            seen.add(key)

    # Save to CSV
    df = pd.DataFrame(unique_users)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f'Saved {len(unique_users)} users (reactions + comments) to {OUTPUT_CSV}')
    driver.quit()

if __name__ == '__main__':
    main()
