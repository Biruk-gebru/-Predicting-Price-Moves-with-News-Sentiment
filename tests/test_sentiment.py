from src.sentiment import analyze_sentiment

def test_analyze_sentiment_positive():
    text = "This is a wonderful and amazing day!"
    score = analyze_sentiment(text)
    assert score > 0

def test_analyze_sentiment_negative():
    text = "This is a terrible and horrible disaster."
    score = analyze_sentiment(text)
    assert score < 0

def test_analyze_sentiment_neutral():
    text = "The book is on the table."
    score = analyze_sentiment(text)
    # Should be near 0
    assert -0.1 <= score <= 0.1

def test_analyze_sentiment_empty():
    assert analyze_sentiment("") == 0.0

def test_analyze_sentiment_none():
    assert analyze_sentiment(None) == 0.0
