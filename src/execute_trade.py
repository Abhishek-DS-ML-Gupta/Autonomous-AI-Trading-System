import json
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

def place_order(signal, qty=1):
    """
    Places a BUY or SELL order on Alpaca (paper trading).
    Reads credentials from config/config.json
    """
    # Load credentials
    config = json.load(open("config/config.json"))

    trading_client = TradingClient(
        config["API_KEY"],
        config["API_SECRET"],
        paper=True  # ensures paper-trading mode
    )

    symbol = config["symbol"]

    if signal == "BUY":
        order_data = MarketOrderRequest(
            symbol=symbol,
            qty=qty,
            side=OrderSide.BUY,
            time_in_force=TimeInForce.GTC
        )
        trading_client.submit_order(order_data)
        print(f"✅ Placed BUY order for {qty} share(s) of {symbol}")

    elif signal == "SELL":
        order_data = MarketOrderRequest(
            symbol=symbol,
            qty=qty,
            side=OrderSide.SELL,
            time_in_force=TimeInForce.GTC
        )
        trading_client.submit_order(order_data)
        print(f"❌ Placed SELL order for {qty} share(s) of {symbol}")

    else:
        print("⚖️ No trade executed (HOLD).")

if __name__ == "__main__":
    # Example test call (you can comment this out later)
    place_order("BUY", qty=1)
