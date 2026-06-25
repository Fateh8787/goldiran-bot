import time
from telegram import Bot
from config import BOT_TOKEN, CHANNEL_ID, CHECK_INTERVAL
from sources import get_news

bot = Bot(BOT_TOKEN)

sent_links = set()

print("✅ GoldIranBot Started")

while True:
    try:
        news = get_news()

        for item in news:
            if item["link"] in sent_links:
                continue

            text = f"""🚨 خبر جدید بازار طلا

📰 {item['title']}

🔗 {item['link']}
"""

            bot.send_message(
                chat_id=CHANNEL_ID,
                text=text,
                disable_web_page_preview=True
            )

            print("ارسال شد:", item["title"])

            sent_links.add(item["link"])

        time.sleep(CHECK_INTERVAL)

    except Exception as e:
        print("ERROR:", e)
        time.sleep(30)
if not any(word in item["title"] for word in KEYWORDS):
    continue
