class Product:
    def __init__(self, name, category, supplier, quantity):
        self.name = name
        self.category = category
        self.supplier = supplier
        self.quantity = quantity

    def update_stock(self, amount):
        self.quantity += amount

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

    def generate_report(self):
        return {name: product.quantity for name, product in self.inventory.items()}

# Example usage
supplier1 = Supplier("ABCSuppliers", "123-456-789")
category1 = Category("Electronics")

product1 = Product("Laptop", category1, supplier1, 50)
category1.add_product(product1)

stock = Stock()
stock.add_product(product1)

supplier1.supply_product(product1, 20)
print(stock.generate_report())