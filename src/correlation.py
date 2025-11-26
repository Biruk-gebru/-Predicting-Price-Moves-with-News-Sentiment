import pandas as pd
from scipy.stats import pearsonr

def align_dates(news_df, stock_df):
    """
    Align news and stock datasets by date.
    Assumes both DataFrames have a datetime index or a 'Date' column.
    """
    # Ensure both have datetime index
    if 'Date' in news_df.columns:
        news_df = news_df.set_index('Date')
    if 'Date' in stock_df.columns:
        stock_df = stock_df.set_index('Date')
        
    # Normalize to date only (drop time) to match daily stock data
    news_df.index = pd.to_datetime(news_df.index).normalize()
    stock_df.index = pd.to_datetime(stock_df.index).normalize()
    
    return news_df, stock_df

def calculate_daily_returns(stock_df, column='Close'):
    """
    Calculate daily percentage change in stock price.
    """
    return stock_df[column].pct_change()

def calculate_correlation(sentiment_series, returns_series):
    """
    Calculate Pearson correlation between two series.
    Aligns them by index (date) first.
    """
    # Align data
    aligned_data = pd.concat([sentiment_series, returns_series], axis=1, join='inner').dropna()
    
    if aligned_data.empty:
        return 0.0, 1.0 # Correlation 0, p-value 1 (no significance)
        
    corr, p_value = pearsonr(aligned_data.iloc[:, 0], aligned_data.iloc[:, 1])
    return corr, p_value
