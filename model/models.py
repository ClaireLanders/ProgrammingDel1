class Product:
    def __init__(self, product_id, name, brand, price, style, movement_type, bracelet_material, bracelet_colour, clasp_type, clasp_material, case_diameter, case_material, water_resistance, bezel_material, crystal, dial, power_reserve, image_url, description, stock):
        """
        Represents a product in the ecommerce store.
        """
        self.product_id = product_id
        self.name = name
        self.brand = brand
        self.price = price
        self.style = style  # e.g "smartwatch", "sport", "luxury"
        self.movement_type = movement_type  # e.g., "automatic", "quartz"
        self.bracelet_material = bracelet_material
        self.bracelet_colour = bracelet_colour
        self.clasp_type = clasp_type
        self.clasp_material = clasp_material
        self.case_diameter = case_diameter  # size of the watch face
        self.case_material = case_material
        self.water_resistance = water_resistance
        self.bezel_material = bezel_material
        self.crystal = crystal
        self.dial = dial
        self.power_reserve = power_reserve
        self.imageUrl = image_url
        self.description = description
        self.stock = stock



    def __repr__(self):
        return f"Product({self.name}, {self.brand}, ${self.price})"


class User:
    def __init__(self, user_id, username, email, password, user_type="customer"):
        """
        Represents a user in the ecommerce system.
        """
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.user_type = user_type  # "admin" or "customer"

    def is_admin(self):
        """Checks if the user is an admin."""
        return self.user_type == "admin"

    def __repr__(self):
        return f"User({self.username}, {self.email}, Type: {self.user_type})"


class LineItem:
    def __init__(self, product, quantity):
        """
        Represents an item in a shopping basket or order.
        """
        if not isinstance(product, Product):
            raise ValueError("LineItem must reference a Product.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.product = product
        self.quantity = quantity
        self.total_price = self.product.price * self.quantity

    def __repr__(self):
        return f"LineItem(Product: {self.product.name}, Quantity: {self.quantity}, Total: ${self.total_price:.2f})"


class Basket:
    def __init__(self):
        """
        Represents a user's shopping basket.
        """
        self.items = []

    def add_item(self, product, quantity):
        """Adds an item to the basket."""
        self.items.append(LineItem(product, quantity))

    def remove_item(self, product_id):
        """Removes an item from the basket."""
        self.items = [item for item in self.items if item.product.product_id != product_id]

    def calculate_total(self):
        """Calculates the total price of items in the basket."""
        return sum(item.total_price for item in self.items)

    def get_number_of_items(self):
        """Returns the number of items in the basket."""
        return len(self.items)

    def __repr__(self):
        return f"Basket({self.items})"


class Transaction:
    def __init__(self, transaction_id, user, basket):
        """
        Represents a completed transaction.
        """
        if not isinstance(user, User):
            raise ValueError("Transaction must reference a User.")
        if not isinstance(basket, Basket):
            raise ValueError("Transaction must reference a Basket.")
        self.transaction_id = transaction_id
        self.user = user
        self.basket = basket
        self.total_amount = basket.calculate_total()

    def __repr__(self):
        return f"Transaction(ID: {self.transaction_id}, User: {self.user.username}, Total: ${self.total_amount:.2f})"




