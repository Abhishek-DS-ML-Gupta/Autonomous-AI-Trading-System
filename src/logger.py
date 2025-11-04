import os
import csv
from datetime import datetime

def log_trade(symbol, signal, current_price, predicted_price, qty):
    """
    Logs every trade to logs/trades.csv.
    If the file doesn't exist, it creates it with headers.
    """
    os.makedirs("logs", exist_ok=True)
    log_file = "logs/trades.csv"
    header = ["timestamp", "symbol", "signal", "current_price", "predicted_price", "qty"]

    # Create CSV with header if not exists
    if not os.path.exists(log_file):
        with open(log_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)

    # Append new trade
    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.utcnow().isoformat(),
            symbol,
            signal,
            round(float(current_price), 2),
            round(float(predicted_price), 2),
            qty
        ])
    print(f"🧾 Trade logged → {log_file}")

# ✅ Self-test when run directly
if __name__ == "__main__":
    print("🧪 Running logger self-test...")
    log_trade(
        symbol="AAPL",
        signal="BUY",
        current_price=250.35,
        predicted_price=260.50,
        qty=1
    )
    print("✅ Logger test complete. Check logs/trades.csv for entry.")
