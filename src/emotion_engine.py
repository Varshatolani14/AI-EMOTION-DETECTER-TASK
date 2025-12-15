from textblob import TextBlob

def detect_emotion(text):
    """
    Lightweight emotion detection from text.
    """
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.2:
        return "happy"
    elif polarity < -0.2:
        return "sad"
    else:
        return "neutral"
