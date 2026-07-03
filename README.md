# Binance Futures Trading Bot

## Overview

This project is a Python command-line application that places MARKET and LIMIT orders on the Binance Futures Testnet using the Binance API.

---

## Features

- Place MARKET Orders
- Place LIMIT Orders
- BUY and SELL Support
- Command Line Interface (argparse)
- Input Validation
- Logging
- Exception Handling

---

## Project Structure

```
trading_bot/
│── cli.py
│── client.py
│── orders.py
│── validators.py
│── logging_config.py
│── logs/
│── requirements.txt
│── README.md
│── .env
```

---

## Installation

### Step 1

Clone the repository

```bash
git clone <your-github-repository-url>
```

### Step 2

Move into the project folder

```bash
cd trading_bot
```

### Step 3

Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4

Create a `.env` file

```
API_KEY=YOUR_API_KEY
API_SECRET=YOUR_API_SECRET
```

---

## Usage

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

### SELL MARKET Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

---

## Logging

Logs are automatically stored in

```
logs/trading.log
```

The log file records

- API Requests
- API Responses
- Errors

---

## Assumptions

- Uses Binance Futures Testnet
- Internet connection is required
- API credentials are loaded from a `.env` file

---

## Author

Priti Singh
