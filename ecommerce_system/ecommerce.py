class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.orders = []

    def create_order(self, order):
        self.orders.append(order)
        print(f"Order {order.order_id} created by {self.name}")


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class Order:
    def __init__(self, order_id, user_id, status='pending'):
        self.order_id = order_id
        self.user_id = user_id
        self.status = status
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Added {product.name} to order {self.order_id}")

    def complete_order(self):
        self.status = 'completed'
        print(f"Order {self.order_id} completed.")


class Payment:
    def __init__(self, payment_id, amount, order_id):
        self.payment_id = payment_id
        self.amount = amount
        self.order_id = order_id

    def make_payment(self):
        print(f"Payment of {self.amount} made for order {self.order_id}")


# Add code to create instances and execute functions to see output
if __name__ == "__main__":
    # Create User
    user1 = User(user_id=1, name="Alice", email="alice@example.com")
    
    # Create Products
    product1 = Product(product_id=101, name="Laptop", price=1200.00)
    product2 = Product(product_id=102, name="Headphones", price=150.00)
    
    # Create Order
    order1 = Order(order_id=1001, user_id=user1.user_id)
    user1.create_order(order1)

    # Add Products to Order
    order1.add_product(product1)
    order1.add_product(product2)
    
    # Complete Order
    order1.complete_order()

    # Make Payment
    payment1 = Payment(payment_id=201, amount=1350.00, order_id=order1.order_id)
    payment1.make_payment()
