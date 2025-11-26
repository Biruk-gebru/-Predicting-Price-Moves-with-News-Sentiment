import pandas as pd
import numpy as np

def load_stock_data(filepath):
    """
    Load stock data from a CSV file.
    Expected columns: Date, Open, High, Low, Close, Volume
    """
    df = pd.read_csv(filepath)
    # Ensure column names are standardized (e.g., title case)
    df.columns = [c.title() for c in df.columns]
    
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
    
    return df

def calculate_sma(df, window=20, column='Close'):
    """
    Calculate Simple Moving Average (SMA).
    """
    return df[column].rolling(window=window).mean()

def calculate_rsi(df, window=14, column='Close'):
    """
    Calculate Relative Strength Index (RSI).
    """
    delta = df[column].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    
    # Handle division by zero if loss is 0 (though rare in rolling mean of price changes)
    rsi = rsi.fillna(100) # If no loss, RSI is 100
    
    return rsi

def calculate_macd(df, fast=12, slow=26, signal=9, column='Close'):
    """
    Calculate Moving Average Convergence Divergence (MACD).
    Returns a DataFrame with 'MACD', 'Signal', and 'Hist'.
    """
    ema_fast = df[column].ewm(span=fast, adjust=False).mean()
    ema_slow = df[column].ewm(span=slow, adjust=False).mean()
    
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()
    histogram = macd_line - signal_line
    
    return pd.DataFrame({
        'MACD': macd_line,
        'Signal': signal_line,
        'Hist': histogram
    })
