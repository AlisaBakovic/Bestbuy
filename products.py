class Product:
    def __init__(self, name, price, quantity):
        """Initialize product with name, price, quantity, and active status."""
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Return the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """Set the quantity; deactivate if quantity is 0."""
        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Return True if product is active, False otherwise."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Return a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """Buy a given quantity, update quantity, and return total price."""
        if not self.is_active():
            raise Exception("Cannot buy an inactive product.")

        if quantity <= 0:
            raise Exception("Quantity must be greater than 0.")

        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock.")

        total_price = quantity * self.price

        self.set_quantity(self.quantity - quantity)

        return total_price