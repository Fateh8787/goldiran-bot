import os
import time
import feedparser
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")

print("Bot started")
print("Token:", TOKEN)
CHANNEL_ID = "@goldiran87"

bot = Bot(token=TOKEN)

sent_links = set()

RSS_FEEDS = [
    "https://www.talanews.com/feed"
]

while True:
    try:
        for feed_url in RSS_FEEDS:
            feed = feedparser.parse(feed_url)

            for entry in feed.entries[:10]:
                if entry.link in sent_links:
                    continue

                message = f"""
🚨 خبر جدید بازار طلا

{entry.title}

{entry.link}
"""

                bot.send_message(
                    chat_id=CHANNEL_ID,
                    text=message
                )

                sent_links.add(entry.link)

        time.sleep(300)

    except Exception as e:
        print(e)
        time.sleep(60)
