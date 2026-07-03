def print_order_summary(symbol, side, order_type, quantity, price):
    print("\nORDER SUMMARY")
    print("-" * 30)
    print(f"Symbol: {symbol}")
    print(f"Side: {side}")
    print(f"Type: {order_type}")
    print(f"Quantity: {quantity}")
    if price:
        print(f"Price: {price}")
    print("-" * 30)