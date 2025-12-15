import feedparser

def get_headlines(limit=5):
    """
    Fetch live news headlines (no API key).
    """
    feed = feedparser.parse("https://news.google.com/rss")

    headlines = []
    for entry in feed.entries[:limit]:
        headlines.append(entry.title)

    return headlines
