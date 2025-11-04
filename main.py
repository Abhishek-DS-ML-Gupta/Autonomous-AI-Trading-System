from src.data_fetch import fetch_data
from src.predict import predict_next
from src.trade_logic import trading_signal
from src.execute_trade import place_order
from src.logger import log_trade
import yfinance as yf

if __name__ == "__main__":
    symbol = "AAPL"

    print("🚀 Fetching latest data...")
    fetch_data(symbol)

    print("🤖 Predicting next price...")
    predicted_price = predict_next(symbol)

    # Get current market price (safe scalar extraction)
    data = yf.download(symbol, period="1d", auto_adjust=False)
    current_price = float(data["Close"].tail(1).values[0])
    print(f"💲 Current price of {symbol}: ${current_price:.2f}")

    # Generate trading signal
    signal = trading_signal(current_price, predicted_price)
    print(f"🧭 Final Trading Decision: {signal}")

    # Execute trade safely
    place_order(signal, qty=1)

    # Log trade
    log_trade(symbol, signal, current_price, predicted_price, qty=1)
