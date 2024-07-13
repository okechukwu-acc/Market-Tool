import pandas as pd

def calculate_indicators(data):
    data['MA50'] = data['Close'].rolling(window=50).mean()
    data['MA200'] = data['Close'].rolling(window=200).mean()
    data['RSI'] = compute_rsi(data['Close'])
    data['Bollinger High'], data['Bollinger Low'] = compute_bollinger_bands(data['Close'])
    return data

def compute_rsi(series, period=14):
    delta = series.diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def compute_bollinger_bands(series, window=20, num_of_std=2):
    rolling_mean = series.rolling(window).mean()
    rolling_std = series.rolling(window).std()
    bollinger_high = rolling_mean + (rolling_std * num_of_std)
    bollinger_low = rolling_mean - (rolling_std * num_of_std)
    return bollinger_high, bollinger_low
