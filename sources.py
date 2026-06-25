import feedparser

FEEDS = [
    "https://www.talanews.com/feed",
    "https://www.mehrnews.com/rss",
    "https://www.tasnimnews.com/fa/rss/feed/0/7/0",
    "https://www.irna.ir/rss",
]

KEYWORDS = [
    "طلا",
    "سکه",
    "دلار",
    "ارز",
    "بانک مرکزی",
    "طلای ۱۸ عیار",
    "اونس",
]

def get_news():
    news = []

    for feed_url in FEEDS:
        try:
            feed = feedparser.parse(feed_url)

            for item in feed.entries:
                title = item.get("title", "")
                link = item.get("link", "")

                if not any(word in title for word in KEYWORDS):
                    continue

                news.append({
                    "title": title,
                    "link": link
                })

        except Exception as e:
            print("RSS ERROR:", e)

    return news
