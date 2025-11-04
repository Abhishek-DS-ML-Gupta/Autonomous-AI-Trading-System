import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

def train_lstm(symbol="AAPL"):
    path = f"data/{symbol}.csv"
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} not found. Run data_fetch.py first.")

    # --- Load CSV safely ---
    df = pd.read_csv(path)
    df.columns = [c.strip().lower() for c in df.columns]  # normalize names

    # Try to find the best column for closing price
    possible_close = [c for c in df.columns if "close" in c]
    if not possible_close:
        raise KeyError("No 'Close' or similar column found in the CSV file.")
    close_col = possible_close[0]

    # Keep only numeric close prices
    df = df[[close_col]].dropna()
    df.rename(columns={close_col: "close"}, inplace=True)
    df["close"] = pd.to_numeric(df["close"], errors="coerce")
    df.dropna(inplace=True)

    # --- Prepare scaled data ---
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(df["close"].values.reshape(-1, 1))

    X, y = [], []
    seq_len = 60
    for i in range(seq_len, len(scaled)):
        X.append(scaled[i - seq_len:i, 0])
        y.append(scaled[i, 0])
    X, y = np.array(X), np.array(y)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    # --- Build LSTM model ---
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)),
        Dropout(0.2),
        LSTM(50),
        Dropout(0.2),
        Dense(25),
        Dense(1)
    ])
    model.compile(optimizer="adam", loss="mean_squared_error")

    print("🚀 Training started...")
    history = model.fit(X, y, epochs=20, batch_size=32, validation_split=0.1, verbose=1)

    # --- Save model ---
    os.makedirs("models", exist_ok=True)
    model.save("models/lstm_model.h5")
    print("✅ Model trained and saved successfully at models/lstm_model.h5")

if __name__ == "__main__":
    train_lstm()
