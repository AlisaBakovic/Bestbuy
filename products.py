class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self. quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if not self.is_active():
            raise Exception("Cannot buy an inactive product.")

        if quantity <= 0:
            raise Exception("Quantity must be greater than 0.")

        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock.")

        total_price = quantity * self.price

        self.set_quantity(self.quantity - quantity)

        return total_price




