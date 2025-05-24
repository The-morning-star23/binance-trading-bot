import argparse
from bot import BasicBot
import logging
from config import API_KEY, API_SECRET
from logger import setup_logging
from rich import print
from rich.console import Console

setup_logging()
console = Console()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot CLI")
    parser.add_argument("symbol", help="Trading symbol like BTCUSDT")
    parser.add_argument("side", choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("type", choices=["MARKET", "LIMIT", "STOP_MARKET"], help="Order type")
    parser.add_argument("quantity", type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")
    parser.add_argument("--stop_price", type=float, help="Required for STOP_MARKET orders")

    args = parser.parse_args()

    bot = BasicBot(API_KEY, API_SECRET)

    order = bot.place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price,
        stop_price=args.stop_price
    )

    if order:
        console.print(f"[green]Order successfully placed![/green]\n{order}")
    else:
        console.print("[red]Order failed. Check logs for details.[/red]")

if __name__ == "__main__":
    main()
