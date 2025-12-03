class Store:
    def __init__(self, product_list):
        """Initialize store with a list of products."""
        self.products = product_list

    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store or raise exception if not found."""
        if product in self.products:
            self.products.remove(product)
        else:
            raise Exception("Product not found in store.")

    def get_total_quantity(self):
        """Return total quantity of all products in the store."""
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        """Return a list of all active products in the store."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        """Buy multiple products and return the total price."""
        total_price = 0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price

