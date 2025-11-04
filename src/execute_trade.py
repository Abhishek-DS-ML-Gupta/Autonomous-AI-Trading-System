import json
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from src.logger import log_trade

def place_order(signal, current_price, predicted_price, qty=1):
    """Execute a market order on Alpaca (paper)."""
    with open("config/config.json") as f:
        config = json.load(f)

    symbol = config["symbol"]
    trading_client = TradingClient(config["API_KEY"], config["API_SECRET"], paper=True)

    if signal == "HOLD":
        print("⚖️ No trade executed (HOLD).")
        return

    side = OrderSide.BUY if signal == "BUY" else OrderSide.SELL
    order_req = MarketOrderRequest(symbol=symbol, qty=qty, side=side, time_in_force=TimeInForce.GTC)

    try:
        order = trading_client.submit_order(order_req)
        print(f"✅ {signal} order placed for {qty} share(s) of {symbol}")
        log_trade(symbol, signal, current_price, predicted_price, qty)
    except Exception as e:
        print(f"❌ Trade failed: {e}")
