import pandas as pd
from src.eda import headline_length_stats, articles_per_publisher, publications_over_time


def make_sample_df():
    data = [
        {"headline": "Company A beats earnings expectations", "publisher": "NewsOne", "date": "2025-11-20"},
        {"headline": "Company B issues dividend", "publisher": "NewsTwo", "date": "2025-11-20"},
        {"headline": "Company A announces new product", "publisher": "NewsOne", "date": "2025-11-21"},
    ]
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    return df


def test_headline_length_stats():
    df = make_sample_df()
    stats = headline_length_stats(df)
    # expect count == 3
    assert int(stats["count"]) == 3


def test_articles_per_publisher():
    df = make_sample_df()
    counts = articles_per_publisher(df)
    assert counts["NewsOne"] == 2
    assert counts["NewsTwo"] == 1


def test_publications_over_time():
    df = make_sample_df()
    ts = publications_over_time(df, freq="D")
    # dates present: 2025-11-20 => 2, 2025-11-21 => 1
    d20 = pd.to_datetime("2025-11-20")
    d21 = pd.to_datetime("2025-11-21")
    assert ts.loc[d20] == 2
    assert ts.loc[d21] == 1
