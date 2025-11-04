import yfinance as yf
import os

def fetch_data(symbol="AAPL", period="1y", interval="1d"):
    """Fetch historical stock data and save to CSV."""
    os.makedirs("data", exist_ok=True)
    print(f"🚀 Fetching data for {symbol} ...")

    data = yf.download(symbol, period=period, interval=interval)
    if data.empty:
        raise ValueError("❌ No data fetched. Check internet or symbol.")

    file_path = f"data/{symbol}.csv"
    data.to_csv(file_path)
    print(f"✅ Data saved → {file_path}")
    return data

if __name__ == "__main__":
    fetch_data()
