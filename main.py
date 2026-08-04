import os
import requests

SITE_URL = "https://hooshmandyadak.ir"

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = "@hooshmandYadak"


def send_telegram():

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    message = """
✅ تست اتصال هوشمند یدک

ربات تلگرام با موفقیت به GitHub Actions متصل شد.

🔧 هوشمند یدک
🌐 hooshmandyadak.ir

#هوشمند_یدک
#لوازم_یدکی_خودرو
"""

    keyboard = {
        "inline_keyboard": [
            [
                {
                    "text": "🔗 مشاهده در سایت",
                    "url": SITE_URL
                }
            ]
        ]
    }

    data = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "reply_markup": keyboard,
        "parse_mode": "HTML"
    }

    response = requests.post(
        url,
        data=data
    )

    print(response.text)


if __name__ == "__main__":
    send_telegram()
