import os
import csv
from datetime import datetime

def log_trade(symbol, signal, current_price, predicted_price, qty):
    """Save trade info into logs/trades.csv"""
    os.makedirs("logs", exist_ok=True)
    file_path = "logs/trades.csv"
    header = ["timestamp", "symbol", "signal", "current_price", "predicted_price", "qty"]

    if not os.path.exists(file_path):
        with open(file_path, "w", newline="") as f:
            csv.writer(f).writerow(header)

    with open(file_path, "a", newline="") as f:
        csv.writer(f).writerow([
            datetime.utcnow().isoformat(),
            symbol, signal,
            round(float(current_price), 2),
            round(float(predicted_price), 2),
            qty
        ])

    print(f"🧾 Trade logged → {file_path}")
