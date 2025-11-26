import pandas as pd
import numpy as np
from src.indicators import calculate_sma, calculate_rsi, calculate_macd

def make_sample_stock_df():
    # Create a simple increasing price series
    dates = pd.date_range(start='2025-01-01', periods=50, freq='D')
    prices = np.linspace(100, 150, 50)
    # Add some noise to make RSI interesting
    prices[10:20] -= 5 
    df = pd.DataFrame({'Close': prices}, index=dates)
    return df

def test_calculate_sma():
    df = make_sample_stock_df()
    sma = calculate_sma(df, window=10)
    # First 9 values should be NaN
    assert pd.isna(sma.iloc[8])
    assert not pd.isna(sma.iloc[9])
    # SMA should be close to the mean of the window
    assert np.isclose(sma.iloc[9], df['Close'].iloc[:10].mean())

def test_calculate_rsi():
    df = make_sample_stock_df()
    rsi = calculate_rsi(df, window=14)
    # RSI should be between 0 and 100
    assert rsi.min() >= 0
    assert rsi.max() <= 100
    # Check shape
    assert len(rsi) == len(df)

def test_calculate_macd():
    df = make_sample_stock_df()
    macd_df = calculate_macd(df)
    assert 'MACD' in macd_df.columns
    assert 'Signal' in macd_df.columns
    assert 'Hist' in macd_df.columns
    assert len(macd_df) == len(df)
