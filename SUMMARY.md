# Simple Summary — EDA & Sentiment Analysis

This is a short, plain summary focusing on the EDA and sentiment-correlation work you ran in the notebooks. Keep this as your project summary to add to GitHub.

## Datasets used

- News / analyst ratings: `Data/raw_analyst_ratings.csv` (columns used: `date`, `stock`, `headline`).
- Stock price files: `Data/Data/<TICKER>.csv` or `data/stocks/<TICKER>.csv` for AAPL, AMZN, GOOG, META, MSFT, NVDA.
- Notebook-derived CSVs (quick summaries): `notebooks/output/*.csv` and `output/*.csv` (headline stats, publisher counts, top words).

## EDA — key points

- Headline length: measured and saved (headline length distribution helps assess data quality).
- Top headline words: frequent words and topics were extracted (useful to spot dominant themes).
- Publisher/time trends: publication counts over time reveal activity spikes.
- Artifacts: CSVs for these summaries are present. Visual plots were created in notebooks but I did not find exported image files in the repo.

Practical takeaway: EDA shows the news coverage volume, common topics, and basic text quality (lengths, empties).

## Sentiment analysis & correlation — key points

- Sentiment generation: headlines are passed to `src.sentiment.analyze_sentiment` and averaged per day.
- Return calculation: stock daily returns are computed in `src.correlation.calculate_daily_returns`.
- Correlation: notebooks compute Pearson correlation and a p-value between daily sentiment and same-day returns and show a scatter plot.
- Typical result: correlation may be weak/insignificant for short windows — interpret carefully (small samples, noisy headlines).

Practical takeaway: sentiment signals can complement indicators, but they need careful alignment (market days) and more data to reach stable conclusions.

## Issues faced (observed / likely)

1. Missing image exports: notebooks produce plots but PNG/JPG/SVG files were not found — add `plt.savefig(...)` after plotting to persist visuals.
2. Path inconsistencies: data exists under both `Data/` and `data/` folders; keep one consistent path to avoid FileNotFound errors.
3. Date column formats: notebooks lowercase columns then expect `date` -> convert to datetime carefully; some files use ISO formats or different names (`Date` vs `date`).
4. Small sample sizes / alignment: daily aggregation reduces sample size; aligning news dates with market trading days (holidays/weekends) matters.
5. Sentiment model limitations: simple headline-level sentiment can be noisy; consider weighting by publisher or using headline context.

Add these as notes in your report or README so other readers know the constraints.

## How to save figures and push to GitHub (quick)

1) Make a figures folder:

```bash
mkdir -p notebooks/figures
```

2) In plotting cells, add after plotting, for example:

```python
plt.tight_layout()
plt.savefig('notebooks/figures/figure_name.png', dpi=150)
plt.show()
```

3) Stage and push files to GitHub from the project root:

```bash
git add SUMMARY.md notebooks/figures/*.png
git commit -m "Add simple summary and notebook figures"
git push origin $(git rev-parse --abbrev-ref HEAD)
```

If you prefer, I can run the `git add`/`git commit` here for `SUMMARY.md` (and any figures you create). Tell me to proceed.

## Final short note

This file is intended to be your concise summary for the repository. If you want, I can also:
- Add `plt.savefig` lines into the notebooks automatically, or
- Run the git commit for `SUMMARY.md` now.

Let me know which next step you want.