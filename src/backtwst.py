import pandas as pd

def backtest(df):
    df['Signal'] = (df['Close'].shift(-1) > df['Close']).astype(int)
    df['Return'] = df['Close'].pct_change()
    df['Strategy'] = df['Signal'].shift(1) * df['Return']

    cum_strategy = (1 + df['Strategy']).cumprod()
    cum_market = (1 + df['Return']).cumprod()

    print("📊 Backtest Results:")
    print("Strategy return:", cum_strategy.iloc[-1])
    print("Market return:", cum_market.iloc[-1])
