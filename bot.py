import time
from telegram import Bot
from config import BOT_TOKEN, CHANNEL_ID, CHECK_INTERVAL
from sources import get_news
from database import init_db, exists, save

bot = Bot(BOT_TOKEN)

init_db()

print("✅ GoldIranBot Started")

while True:
    try:
        news = get_news()

        for item in news:

            if exists(item["link"]):
                continue

            text = f"""🚨 خبر فوری بازار طلا

📰 {item['title']}

🔗 {item['link']}
"""
price = get_gold_price()

if price:
    text += "\n\n📈 قیمت لحظه‌ای نیز در دسترس است."
            bot.send_message(
                chat_id=CHANNEL_ID,
                text=text,
                disable_web_page_preview=True
            )

            save(item["link"], item["title"])

            print("✅ Sent:", item["title"])

        time.sleep(CHECK_INTERVAL)

    except Exception as e:
        print("❌ ERROR:", e)
        time.sleep(30)
from price import get_gold_price
