# Task 1 Findings Summary
## Predicting Price Moves with News Sentiment - Week 1

**Date**: November 25, 2025  
**Branch**: `task-1`  
**Status**: Ready for merge to `main`

---

## Executive Summary

Task 1 successfully established the foundational infrastructure for analyzing the relationship between financial news sentiment and stock price movements. The work includes a complete project scaffold, exploratory data analysis (EDA) tools, sentiment analysis capabilities, technical indicators, and correlation analysis frameworks.

**Key Achievement**: Created a robust, modular codebase with 5 commits addressing data path configuration, notebook compatibility, and date handling issues.

---

## Commits Overview

The `task-1` branch contains **5 commits** with the following improvements:

| Commit | Description | Impact |
|--------|-------------|--------|
| `72c3fa6` | Add notebook troubleshooting guide and improve sentiment notebook formatting | Documentation + UX |
| `83c7d1b` | Fix date parsing in sentiment notebook to handle dates without timezone | Bug fix |
| `daa76b3` | Fix notebook paths to use correct relative paths from notebooks/ directory | Bug fix |
| `3a223fe` | Fix notebook metadata and formatting for proper VS Code display | Compatibility |
| `4306af7` | Update data paths to use Data/ directory structure | Configuration |

---

## Technical Implementation

### 1. Exploratory Data Analysis (`src/eda.py`)

**Purpose**: Analyze news dataset characteristics and publishing patterns

**Key Functions**:
- `load_news()` - Loads news CSV with automatic date parsing and UTC timezone handling
- `headline_length_stats()` - Computes descriptive statistics for headline lengths
- `articles_per_publisher()` - Counts and ranks publishers by article volume
- `publications_over_time()` - Time series analysis with configurable frequency (daily/weekly)

**Features**:
- Defensive programming with graceful error handling
- Automatic timezone-aware datetime parsing
- Flexible resampling for temporal analysis

### 2. Sentiment Analysis (`src/sentiment.py`)

**Purpose**: Extract sentiment polarity from news headlines

**Implementation**:
- Uses TextBlob for sentiment scoring
- Returns polarity scores from -1.0 (negative) to +1.0 (positive)
- Handles non-string inputs gracefully (returns 0.0)

**Considerations**:
- TextBlob provides general-purpose sentiment analysis
- For finance-specific sentiment, consider upgrading to VADER or FinBERT
- Current implementation is fast and suitable for baseline analysis

### 3. Correlation Analysis (`src/correlation.py`)

**Purpose**: Measure relationships between sentiment and stock returns

**Key Functions**:
- `align_dates()` - Synchronizes news and stock data by date
- `calculate_daily_returns()` - Computes percentage change in stock prices
- `calculate_correlation()` - Pearson correlation with statistical significance (p-values)

**Features**:
- Automatic date normalization for daily alignment
- Inner join to handle missing data
- Returns both correlation coefficient and p-value for significance testing

### 4. Technical Indicators (`src/indicators.py`)

**Purpose**: Calculate stock market technical indicators

**Implemented Indicators**:
- **SMA (Simple Moving Average)**: Configurable window (default: 20 days)
- **RSI (Relative Strength Index)**: Momentum oscillator (default: 14 days)
- **MACD (Moving Average Convergence Divergence)**: Trend-following indicator with signal line

**Features**:
- Pure pandas/numpy implementation (no TA-Lib dependency)
- Handles edge cases (division by zero in RSI)
- Returns structured DataFrames for easy visualization

---

## Notebooks

### `01-EDA.ipynb`
- Headline length distribution analysis
- Top publishers ranking
- Publication frequency time series
- Word frequency analysis

### `02-Indicators.ipynb`
- SMA, RSI, and MACD calculations
- Visualization of technical indicators
- Stock price trend analysis

### `03-Sentiment-Correlation.ipynb`
- Sentiment scoring for news headlines
- Daily sentiment aggregation
- Correlation analysis between sentiment and stock returns
- Scatter plot visualization

---

## Data Structure

**Expected Data Files** (place in `Data/` directory):

1. **`raw_analyst_ratings.csv`** (News data)
   - Columns: `headline`, `publisher`, `date`, `stock`
   - Date format: ISO 8601 with timezone support

2. **Stock Price Data**
   - Columns: `Date`, `Open`, `High`, `Low`, `Close`, `Volume`
   - Can be fetched using `yfinance` if not available

---

## Key Findings

### 1. **Data Path Configuration**
- ✅ Fixed: All notebooks now use `Data/` directory for consistency
- ✅ Fixed: Relative paths work correctly from `notebooks/` directory
- **Impact**: Eliminates path-related errors when running notebooks

### 2. **Date Handling**
- ✅ Fixed: Timezone-aware datetime parsing prevents errors
- ✅ Fixed: Date normalization ensures proper alignment between news and stock data
- **Impact**: Accurate temporal correlation analysis

### 3. **Notebook Compatibility**
- ✅ Fixed: VS Code notebook metadata formatting
- ✅ Added: `NOTEBOOK_FIX.md` with solutions for VS Code Service Worker issues
- **Impact**: Improved developer experience across different environments

### 4. **Modular Architecture**
- ✅ Implemented: Separation of concerns (EDA, sentiment, correlation, indicators)
- ✅ Implemented: Reusable functions with clear interfaces
- **Impact**: Easy to extend and test individual components

---

## Testing

**Test Coverage**:
- `tests/test_eda.py` - EDA functions validation
- `tests/test_indicators.py` - Technical indicator calculations
- `tests/test_sentiment.py` - Sentiment analysis accuracy

**CI/CD**:
- GitHub Actions workflow configured for automated testing
- Runs on push and pull request events

---

## Known Issues & Solutions

### Issue: VS Code Notebook Service Worker Error

**Problem**: VS Code may fail to initialize notebooks with Service Worker errors

**Solutions** (documented in `NOTEBOOK_FIX.md`):
1. Clear VS Code Service Worker cache: `rm -rf ~/.config/Code/Service\ Worker/`
2. Use Jupyter Notebook in browser: `jupyter notebook`
3. Use Jupyter Lab: `jupyter lab`

**Note**: This is a VS Code bug, not a notebook validity issue. All notebooks are properly formatted.

---

## Statistical Insights (Preliminary)

Based on the implemented analysis framework:

1. **Sentiment Distribution**: TextBlob polarity scores range from -1 to +1
2. **Correlation Method**: Pearson correlation with p-value significance testing
3. **Temporal Alignment**: Daily aggregation of sentiment matched with daily stock returns
4. **Data Quality**: Automatic handling of missing data through inner joins

---

## Next Steps & Recommendations

### Immediate (Post-Merge)
1. ✅ Merge `task-1` to `main` via pull request
2. Run EDA on complete dataset and generate visualizations
3. Compute sentiment-return correlations for multiple stocks (AAPL, TSLA, etc.)
4. Document correlation findings with statistical significance

### Short-Term Enhancements
1. **Sentiment Upgrade**: Implement FinBERT or VADER for finance-specific sentiment
2. **Multi-Day Analysis**: Test 3-day, 5-day, and 7-day return correlations
3. **Statistical Validation**: Add confidence intervals and hypothesis testing
4. **Visualization**: Create publication-quality plots (up to 10 as per requirements)

### Long-Term Improvements
1. **Feature Engineering**: Add lagged sentiment features
2. **Machine Learning**: Build predictive models using sentiment + technical indicators
3. **Real-Time Pipeline**: Implement streaming sentiment analysis
4. **Portfolio Analysis**: Extend to multiple stocks simultaneously

---

## Dependencies

```
pandas
numpy
scipy
textblob
matplotlib
jupyter
pytest
```

**Optional**: `yfinance` for fetching stock price data

---

## How to Use This Work

### 1. Setup Environment
```bash
pip install -r requirements.txt
```

### 2. Prepare Data
Place CSV files in `Data/` directory:
- `raw_analyst_ratings.csv` (news data)
- Stock price CSVs (or fetch with yfinance)

### 3. Run EDA
```bash
python -m src.run_eda
```

### 4. Explore Notebooks
```bash
jupyter notebook
# Navigate to notebooks/ directory
```

### 5. Run Tests
```bash
pytest tests/
```

---

## Conclusion

Task 1 has successfully delivered a production-ready foundation for sentiment-driven stock analysis. The codebase is:

- ✅ **Modular**: Clear separation of concerns
- ✅ **Tested**: Unit tests for core functionality
- ✅ **Documented**: Comprehensive docstrings and README
- ✅ **Robust**: Defensive error handling and edge case management
- ✅ **Extensible**: Easy to add new features and indicators

