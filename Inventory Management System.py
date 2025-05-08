class Product:
    def __init__(self, name, category, supplier, quantity):
        self.name = name
        self.category = category
        self.supplier = supplier
        self.quantity = quantity

        # __**Added stock level threshold attribute**__
        self.min_stock = 10  # Default low stock threshold

    def update_stock(self, amount):
        self.quantity += amount

    # __**Added method to check low stock status**__
    def is_low_stock(self):
        return self.quantity < self.min_stock

class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.purchase_history = []

    def purchase_product(self, product, quantity):
        if product.quantity >= quantity:
            product.update_stock(-quantity)
            self.purchase_history.append({
                "product": product.name,
                "quantity": quantity
            })
        else:
            raise ValueError("Insufficient stock to complete the purchase")

class Category:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

class Supplier:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def supply_product(self, product, quantity):
        product.update_stock(quantity)

class Stock:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product):
        self.inventory[product.name] = product

     # __**Modified report to include low stock warning**__
    def generate_report(self):
        report = {}
        for name, product in self.inventory.items():
            report[name] = {
                "quantity": product.quantity,
                # __**Include low stock alert in report**__
                "low_stock": product.is_low_stock()
            }
        return report

# Example usage
supplier1 = Supplier("ABCSuppliers", "123-456-789")
category1 = Category("Electronics")

product1 = Product("Laptop", category1, supplier1, 50)
category1.add_product(product1)

stock = Stock()
stock.add_product(product1)

supplier1.supply_product(product1, 20)

# __**Print full report including low stock alert**__
print(stock.generate_report())