import argparse
import os
from dotenv import load_dotenv

from bot.client import BinanceClient
from bot.validators import (
    validate_symbol, validate_side,
    validate_order_type, validate_quantity,
    validate_price
)
from bot.orders import print_order_summary
from bot.logging_config import setup_logger

load_dotenv()
logger = setup_logger()

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    try:
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price)

        client = BinanceClient()

        print_order_summary(symbol, side, order_type, quantity, price)

        logger.info(f"Placing order: {symbol} {side} {order_type}")

        order = client.place_order(symbol, side, order_type, quantity, price)

        print("\nORDER RESPONSE")
        print("-" * 30)
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")
        print(f"Avg Price: {order.get('avgPrice')}")
        print("-" * 30)

        logger.info(f"Order Success: {order}")

    except Exception as e:
        logger.error(str(e))
        print("ERROR:", str(e))


if __name__ == "__main__":
    main()