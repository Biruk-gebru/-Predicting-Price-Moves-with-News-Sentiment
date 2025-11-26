"""Exploratory Data Analysis helpers for news dataset

This module provides lightweight functions to compute basic descriptive
statistics for headline text and publishing metadata. It's intentionally
defensive: if no data is available it prints instructions for where to
place CSV files.
"""
from typing import Optional
import pandas as pd


def load_news(csv_path: str = "data/news.csv") -> Optional[pd.DataFrame]:
    """Load news CSV. Expected columns: headline, publisher, date, stock

    Returns None if file not found.
    """
    try:
        df = pd.read_csv(csv_path, parse_dates=["date"])
        return df
    except FileNotFoundError:
        print(f"No news CSV found at {csv_path}. Place your dataset in data/ and retry.")
        return None


def headline_length_stats(df: pd.DataFrame) -> pd.Series:
    """Return descriptive stats for headline lengths."""
    lengths = df["headline"].astype(str).str.len()
    return lengths.describe()


def articles_per_publisher(df: pd.DataFrame) -> pd.Series:
    """Count articles per publisher, descending."""
    return df["publisher"].value_counts()


def publications_over_time(df: pd.DataFrame, freq: str = "D") -> pd.Series:
    """Return a time series of article counts resampled to frequency 'freq'.

    Example freq: 'D' (daily), 'W' (weekly)
    """
    ts = df.set_index("date")["headline"].resample(freq).count()
    return ts


if __name__ == "__main__":
    df = load_news()
    if df is None:
        raise SystemExit(1)

    print("Headline length stats:\n", headline_length_stats(df))
    print("\nTop publishers:\n", articles_per_publisher(df).head(20))
    print("\nPublications (daily) sample:\n", publications_over_time(df).head(20))
