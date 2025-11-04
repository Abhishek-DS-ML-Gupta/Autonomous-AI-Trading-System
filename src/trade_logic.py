def trading_signal(current_price, predicted_price, threshold=0.01):
    """
    Generates BUY / SELL / HOLD signals based on predicted change.
    threshold = 0.01 → 1% difference.
    """
    diff = (predicted_price - current_price) / current_price

    if diff > threshold:
        print(f"📈 Predicted rise of {diff*100:.2f}% → BUY signal")
        return "BUY"
    elif diff < -threshold:
        print(f"📉 Predicted drop of {abs(diff)*100:.2f}% → SELL signal")
        return "SELL"
    else:
        print("⚖️ No major change → HOLD signal")
        return "HOLD"
