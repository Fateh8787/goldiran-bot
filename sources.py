import feedparser

FEEDS = [
    "https://www.talanews.com/feed",
]

def get_news():
    news = []

    for url in FEEDS:
        try:
            feed = feedparser.parse(url)

            for item in feed.entries:
                news.append({
                    "title": item.title,
                    "link": item.link
                })

        except Exception as e:
            print(e)

    return news
