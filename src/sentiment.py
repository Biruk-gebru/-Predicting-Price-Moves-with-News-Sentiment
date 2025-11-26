from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze the sentiment of a text string.
    Returns the polarity score (-1.0 to 1.0).
    """
    if not isinstance(text, str):
        return 0.0
    
    blob = TextBlob(text)
    return blob.sentiment.polarity
