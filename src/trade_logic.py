def trading_signal(current_price, predicted_price, threshold=0.01):
    """
    Returns a trading signal based on the predicted vs current price.
    threshold = % difference for triggering a trade (default: 1%)
    """
    diff = (predicted_price - current_price) / current_price

    if diff > threshold:
        print(f"📈 Predicted rise of {diff*100:.2f}% → BUY signal")
        return "BUY"
    elif diff < -threshold:
        print(f"📉 Predicted drop of {abs(diff)*100:.2f}% → SELL signal")
        return "SELL"
    else:
        print(f"⚖️ Change {diff*100:.2f}% within threshold → HOLD")
        return "HOLD"
