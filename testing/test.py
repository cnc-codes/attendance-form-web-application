import os
import requests
import re
import time

def get_title_from_web(url, retries=10, delay=5):
    for i in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            title_match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)
            if title_match:
                return title_match.group(1).strip()
            else:
                return "No title found"
        except requests.exceptions.RequestException:
            print(f"Attempt {i+1}/{retries} failed. Retrying in {delay} seconds...")
            time.sleep(delay)
    return "Failed to get title after retries"

host = os.environ.get("APP_HOST", "localhost")
port = os.environ.get("APP_PORT", 5000)
web_url = f"http://{host}:{port}"

title = get_title_from_web(web_url)

# Flexible assertion: just check if "Form Absensi" is in the title
assert "Form Absensi" in title, f"Expected 'Form Absensi' in title, got '{title}'"
print("Testing success")