# 🧠 Autonomous AI Trading System (AutoAlpha)
A fully-automated AI-powered stock trading bot built in Python.
It uses LSTM neural networks to predict stock prices and automatically executes BUY / SELL / HOLD decisions via Alpaca’s paper-trading API — all logged securely for analysis.

## 🚀 Features

✅ Fetches live & historical stock data (Yahoo Finance)
✅ Trains an LSTM model to predict next-day closing prices
✅ Generates intelligent BUY / SELL / HOLD trading signals
✅ Executes paper trades automatically on Alpaca
✅ Logs every trade in a CSV file for full transparency
✅ Modular architecture — easily extendable for crypto or other exchanges

📂 Project Structure
```bash
StockPrediction/
│
├── config/
│   └── config.json              # Alpaca API keys & settings
│
├── data/
│   └── AAPL.csv                 # Historical stock data
│
├── models/
│   └── lstm_model.h5            # Trained AI model
│
├── logs/
│   └── trades.csv               # Trade history log
│
├── src/
│   ├── data_fetch.py            # Fetches stock data using yfinance
│   ├── train_model.py           # Trains LSTM model
│   ├── predict.py               # Predicts next price
│   ├── trade_logic.py           # Generates BUY/SELL/HOLD signals
│   ├── execute_trade.py         # Executes trades via Alpaca API
│   └── logger.py                # Logs trades into CSV
│
├── main.py                      # Full pipeline (fetch → predict → trade)
├── requirements.txt             # Dependencies
└── .gitignore                   # Ignore configs, models, data, venv
```

## ⚙️ Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Abhishek-DS-ML-Gupta/Autonomous-AI-Trading-System.git
cd Autonomous-AI-Trading-System
```
## 2️⃣ Create a Virtual Environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / WSL
```bash
python3 -m venv venv
source venv/bin/activate
```
## 3️⃣ Install Requirements
```bash
pip install -r requirements.txt
```
## 🔑 Configuration

Create a file at: config/config.json
```bash
{
  "API_KEY": "YOUR_ALPACA_PAPER_API_KEY",
  "API_SECRET": "YOUR_ALPACA_PAPER_API_SECRET",
  "BASE_URL": "https://paper-api.alpaca.markets",
  "symbol": "AAPL",
  "cash": 10000,
  "risk_per_trade": 0.05
}
```

## 🧩 You can get free paper-trading API keys at https://alpaca.markets

## 🧩 Running the Project (Step by Step)
### Step 1 – Fetch Stock Data
```bash
python src/data_fetch.py
```

✅ Downloads data to data/AAPL.csv

### Step 2 – Train LSTM Model
```bash
python src/train_model.py
```

✅ Saves model to models/lstm_model.h5

### Step 3 – Make a Prediction
```bash
python src/predict.py
```

✅ Prints the predicted next-day close price.

### Step 4 – Run the Full Bot
```bash
python main.py
```

### ✅ Complete automated workflow:
```bash
Fetch → Predict → Decide → Trade → Log
```
## Example output:
```bash
🚀 Fetching latest data...
🤖 Predicting next price...
💲 Current price of AAPL: $269.05
📉 Predicted drop of 11.73% → SELL
✅ SELL order placed for 1 share(s) of AAPL
🧾 Trade logged → logs/trades.csv
🧭 Final Trading Decision: SELL
```
## 📊 Trade Log Example
```bash
timestamp,symbol,signal,current_price,predicted_price,qty
2025-11-04T08:30:00Z,AAPL,SELL,269.05,237.49,1
```

## 🧠 How It Works (Overview)
Step	Module	Description
```bash
1️⃣	data_fetch.py	Fetches stock data from Yahoo Finance
2️⃣	train_model.py	Builds and trains the LSTM model
3️⃣	predict.py	Predicts next-day closing price
4️⃣	trade_logic.py	Compares prices → decides BUY/SELL/HOLD
5️⃣	execute_trade.py	Sends trade to Alpaca (paper)
6️⃣	logger.py	Logs decision and trade to CSV
7️⃣	main.py	Orchestrates the full pipeline
```
## 🧰 Technologies Used
Tool	Purpose
```bash
Python 3.12	Core language
TensorFlow / Keras	LSTM model
pandas / NumPy	Data processing
scikit-learn	Data scaling
yfinance	Stock market data
alpaca-py	Trading API
CSV Logging	Trade history tracking
```
