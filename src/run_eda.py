"""Command-line runner for basic EDA tasks.

This script loads `data/news.csv` (if present), prints headline stats,
writes a small summary to `output/eda_summary.csv`, and exits.
"""
from pathlib import Path
import pandas as pd
from src.eda import headline_length_stats, articles_per_publisher, publications_over_time, load_news


def ensure_output_dir():
    out = Path("output")
    out.mkdir(exist_ok=True)
    return out


def run(csv_path: str = "data/news.csv"):
    df = load_news(csv_path)
    if df is None:
        return 1

    stats = headline_length_stats(df)
    top_publishers = articles_per_publisher(df).head(20)
    pub_ts = publications_over_time(df).fillna(0).astype(int)

    out = ensure_output_dir()
    # write small summaries
    stats.to_csv(out / "headline_length_stats.csv")
    top_publishers.to_csv(out / "top_publishers.csv")
    pub_ts.to_csv(out / "publications_over_time.csv")

    print("Wrote EDA summaries to ./output/")
    print(stats)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
