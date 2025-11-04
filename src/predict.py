import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import os

def predict_next(symbol="AAPL"):
    model_path = "models/lstm_model.h5"
    data_path = f"data/{symbol}.csv"

    # Check file existence
    if not os.path.exists(model_path):
        raise FileNotFoundError("❌ Model not found. Run train_model.py first.")
    if not os.path.exists(data_path):
        raise FileNotFoundError("❌ Data not found. Run data_fetch.py first.")

    # Load and clean CSV
    df = pd.read_csv(data_path)
    df.columns = [c.strip().lower() for c in df.columns]  # normalize headers

    # Auto-detect close column
    possible_close = [c for c in df.columns if "close" in c]
    if not possible_close:
        raise KeyError("❌ No 'Close' or similar column found in CSV.")
    close_col = possible_close[0]

    # Extract close column and clean numeric values
    df = df[[close_col]].copy()
    df.rename(columns={close_col: "close"}, inplace=True)
    df["close"] = pd.to_numeric(df["close"], errors="coerce")  # convert safely
    df.dropna(inplace=True)  # remove any rows that couldn't be converted

    if len(df) < 61:
        raise ValueError("❌ Not enough rows in data for prediction (need at least 61).")

    # Scale closing prices
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(df["close"].values.reshape(-1, 1))

    # Prepare last 60 data points
    last_60 = scaled[-60:]
    X_test = np.reshape(last_60, (1, 60, 1))

    # Load model and predict
    model = load_model(model_path)
    pred_scaled = model.predict(X_test)
    pred = scaler.inverse_transform(pred_scaled)[0][0]

    print("✅ Prediction complete")
    print(f"📈 Predicted next closing price for {symbol.upper()}: ${pred:.2f}")
    return pred

if __name__ == "__main__":
    predict_next()
