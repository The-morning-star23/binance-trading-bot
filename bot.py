from binance.client import Client
from binance.enums import *
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        # Setup logging once when initializing the bot
        logging.basicConfig(
            filename='trading_bot.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
        )

        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.API_URL = 'https://testnet.binance.vision/api'
        
        logging.info("Bot initialized on testnet" if testnet else "Bot initialized on live")

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            print(f"Placing order: symbol={symbol}, side={side}, type={order_type}, qty={quantity}, price={price}, stop_price={stop_price}")

            if order_type == 'MARKET':
                order = self.client.create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )
            elif order_type == 'LIMIT' and price is not None:
                order = self.client.create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity,
                    price=price,
                    timeInForce=TIME_IN_FORCE_GTC
                )
            else:
                raise ValueError("Invalid order parameters.")

            logging.info(f"Order placed: {order}")
            return order
        
        except Exception as e:
            logging.error(f"Order error: {e}")
            print(f"Error placing order: {e}")
            return None
