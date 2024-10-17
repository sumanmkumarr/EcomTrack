def process_orders(products, orders):
    """
    Takes a list of products with their current stock levels and a list of orders.
    Reduces stock levels based on orders.
    Triggers a restock alert if stock drops below threshold.
    """
    threshold = 10
    for order in orders:
        product_id = order['product_id']
        quantity = order['quantity']
        if products[product_id]['stock'] >= quantity:
            products[product_id]['stock'] -= quantity
            print(f"Processed order for {quantity} units of {products[product_id]['name']}.")
            if products[product_id]['stock'] < threshold:
                print(f"Alert: {products[product_id]['name']} needs restocking!")
        else:
            print(f"Error: Not enough stock for {products[product_id]['name']}.")


def restock_items(products, restock_list):
    """
    Takes a list of products that need restocking and their required quantities.
    Updates the stock levels.
    """
    for item in restock_list:
        product_id = item['product_id']
        quantity = item['quantity']
        products[product_id]['stock'] += quantity
        print(f"Restocked {quantity} units of {products[product_id]['name']}.")


# Add code to execute the functions and see output
if __name__ == "__main__":
    products = {
        1: {'name': 'Laptop', 'stock': 15},
        2: {'name': 'Phone', 'stock': 5},
        3: {'name': 'Tablet', 'stock': 20}
    }

    orders = [
        {'product_id': 1, 'quantity': 3},
        {'product_id': 2, 'quantity': 6},  # Should trigger out of stock alert
        {'product_id': 3, 'quantity': 2}
    ]

    restock_list = [
        {'product_id': 2, 'quantity': 10}
    ]

    # Process the orders
    process_orders(products, orders)

    # Restock items
    restock_items(products, restock_list)
