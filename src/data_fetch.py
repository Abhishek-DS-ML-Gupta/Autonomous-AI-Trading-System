import yfinance as yf
import pandas as pd

def fetch_data(symbol="AAPL", start="2018-01-01", end="2025-01-01"):
    data = yf.download(symbol, start=start, end=end)
    data.to_csv(f"data/{symbol}.csv")
    return data

if __name__ == "__main__":
    df = fetch_data()
    print(df.tail())
