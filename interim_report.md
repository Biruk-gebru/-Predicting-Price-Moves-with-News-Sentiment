# Interim Report — Week 1 (Partial)

Date: 2025-11-24

## Summary (<= 1 page)

This interim report covers completion of Task 1 (project scaffold, EDA starter work) and partial progress on Task 2 (technical indicators skeleton). The goal is to analyze the relationship between financial news headline sentiment and stock price movements.

Work completed so far:
- Project scaffold and recommended repository structure added.
- `.github` workflow for unit tests added.
- `progress.md` tracker created and kept up-to-date.
- EDA starter notebook (`notebooks/01-EDA.ipynb`) and an executable runner (`src/run_eda.py`) were added. These compute headline-length statistics, publisher counts, and publication frequency time series.
- Technical indicators notebook (`notebooks/02-Indicators.ipynb`) added with SMA, RSI, and MACD implementations (pandas fallback available).
- Sentiment & correlation notebook (`notebooks/03-Sentiment-Correlation.ipynb`) added with TextBlob-based scoring and a simple daily-aggregation + Pearson correlation example.

## Data and assumptions

- Expected datasets (place in `data/`):
  - `news.csv`: columns `headline`, `publisher`, `date`, `stock`.
  - `prices.csv`: columns `date`, `Open`, `High`, `Low`, `Close`, `Volume`.
- Assumptions made:
  - Publication timestamps are parseable by pandas and will be aligned by date (trading day) when computing correlations.
  - TA-Lib may not be available in all environments; fallbacks using pandas are included to compute indicators reliably without native extensions.

## Methods implemented (short)

- EDA: headline length distribution, article counts per publisher, publication frequency over time (resample by day/week).
- Indicators: SMA computed by rolling mean; RSI using average gain/loss over window; MACD as difference of EMAs with signal line.
- Sentiment: TextBlob polarity applied per headline, aggregated by date to average daily sentiment.
- Correlation: daily returns computed from closing prices (pct_change) and merged with average daily sentiment; Pearson correlation used as a first test.

## Key findings so far (preliminary)

- The repository and analysis scaffolding are ready for iterative development and data experiments.
- No dataset has yet been committed to the repo. The notebooks contain examples showing how to load user-provided CSVs in `data/`.

## Next steps (before final submission)

1. Run EDA on the real dataset: generate plots and include top-10 publishers, headline length distribution, and publication-frequency plots.
2. Populate `data/` with `news.csv` and `prices.csv` for a selected set of tickers. If price data is missing, fetch it with `yfinance` or `pynance`.
3. Run sentiment pipeline and compute daily correlations for a small set of stocks (e.g., AAPL, TSLA) to validate approach.
4. If correlation signals are promising, extend to multi-day windows (e.g., next-day return, 3-day return) and test statistical significance (p-values, confidence intervals).
5. Prepare the final report (publication-style) including up to 10 plots.

## How to run what exists now

1. Place CSVs in `data/` as described above.
2. From the repo root, run the EDA runner:

```bash
python -m src.run_eda
```

3. Open the notebooks in `notebooks/` and run cells interactively.

## Challenges / Risks

- TA-Lib installation may require OS-level dependencies on some machines; the notebook provides fallbacks.
- Sentiment analysis with TextBlob is simple (polarity scores) and may not capture finance-specific nuances — consider VADER, FinBERT or a finetuned model for better results.

---

Prepared by: analysis scaffolding auto-generated on behalf of the author. This is a working draft intended for iteration.
