import os
import requests
from bs4 import BeautifulSoup
import hashlib
import json
from datetime import datetime

SITE_URL = "https://hooshmandyadak.ir"

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = "@hooshmandYadak"

DATA_FILE = "sent_posts.json"


def load_sent():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save_sent(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_page():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        SITE_URL,
        headers=headers,
        timeout=20
    )

    response.raise_for_status()

    return BeautifulSoup(
        response.text,
        "html.parser"
    )


def create_id(title, link):
    text = title + link
    return hashlib.md5(
        text.encode()
    ).hexdigest()


def send_telegram(text, link):

    url = (
        f"https://api.telegram.org/"
        f"bot{TELEGRAM_TOKEN}/sendMessage"
    )

    keyboard = {
        "inline_keyboard": [
            [
                {
                    "text": "🔗 مشاهده در سایت",
                    "url": link
                }
            ]
        ]
    }

    data = {
        "chat_id": CHANNEL_ID,
        "text": text,
        "reply_markup": json.dumps(keyboard),
        "parse_mode": "HTML"
    }

    requests.post(
        url,
        data=data
    )


def main():

    soup = get_page()

    sent = load_sent()

    products = []

    # فعلاً تست اولیه
    title = soup.title.text.strip()

    link = SITE_URL

    post_id = create_id(title, link)

    if post_id not in sent:

        text = f"""
🛒 <b>{title}</b>

🔧 جدیدترین محصولات و مقالات هوشمند یدک

#هوشمند_یدک
#لوازم_یدکی_خودرو
"""

        send_telegram(
            text,
            link
        )

        sent.append(post_id)

        save_sent(sent)


if __name__ == "__main__":
    main()
