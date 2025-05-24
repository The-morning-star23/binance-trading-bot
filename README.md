# Binance Futures Testnet Trading Bot

A simple Python bot that places market, limit, and stop-market orders using Binance Futures Testnet.

## Features

- Place BUY/SELL orders
- Supports MARKET, LIMIT, and STOP_MARKET orders
- Command-line interface with validation
- Logs all requests/responses
- Rich terminal output

## Usage

```bash
python cli.py BTCUSDT BUY MARKET 0.01
python cli.py BTCUSDT SELL LIMIT 0.01 --price 30000
python cli.py BTCUSDT BUY STOP_MARKET 0.01 --stop_price 29500
