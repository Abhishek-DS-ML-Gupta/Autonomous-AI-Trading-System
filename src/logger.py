import os
import csv
from datetime import datetime

def log_trade(symbol, signal, current_price, predicted_price, qty):
    """Log every executed trade into a CSV file with timestamp."""
    os.makedirs("logs", exist_ok=True)
    log_file = "logs/trades.csv"
    header = ["timestamp", "symbol", "signal", "current_price", "predicted_price", "qty"]

    # Create the log file if it doesn’t exist
    if not os.path.exists(log_file):
        with open(log_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)

    # Append the trade details
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
