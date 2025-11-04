from src.data_fetch import fetch_data
from src.predict import predict_next
from src.trade_logic import trading_signal
from src.execute_trade import place_order
import yfinance as yf
import json

if __name__ == "__main__":
    # Load config
    with open("config/config.json") as f:
        config = json.load(f)
    symbol = config["symbol"]

    print("🚀 Fetching latest data...")
    fetch_data(symbol)

    print("🤖 Predicting next price...")
    predicted_price = predict_next(symbol)

    data = yf.download(symbol, period="1d")
    current_price = float(data["Close"].iloc[-1])
    print(f"💲 Current price of {symbol}: ${current_price:.2f}")

    signal = trading_signal(current_price, predicted_price)
    place_order(signal, current_price, predicted_price, qty=1)

    print(f"🧭 Final Trading Decision: {signal}")
