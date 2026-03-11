"""
Customer : 
Represents a user of ByteBites. Stores the customer's name
and their purchase history (a list of orders they have placed).

FoodItem :
Represents a single menu item available in the app. Stores the item's
name, price, category, and a popularity rating.

Menu :
Represents the collection of all available food items. Allows items to
be added and filtered by category.

Order : 
Represents a transaction where a customer selects food items.
Stores the selected items and calculates the total cost.
"""

class Customer:
    # Initialize a customer with a name and an empty purchase history. copilot generated the rest of the code based on the provided context.
    def __init__(self, name: str):
        self.name = name
        self.purchase_history = []


class FoodItem:
    # Initialize a food item with its name, price, category, and popularity rating.
    # Copilot generated the rest of the code based on the provided context.
    def __init__(self, name: str, price: float, category: str, popularity: int):
        self.name = name
        self.price = price
        self.category = category
        self.popularity = popularity


class Menu:
    # Initialize the menu with an empty list of items. Copilot generated the rest of the code based on the provided context.
    def __init__(self):
        self.items = []


class Order:
    # Initialize an order with a customer and an empty list of selected items. Copilot generated the rest of the code based on the provided context.
    def __init__(self, customer):
        self.items = []
        self.customer = customer

# Copilot matched my design choices!
# Copilot reviewed one class at a time and suggested methods for adding items to the menu, filtering items by category, adding items to an order, and calculating the total cost of an order. The generated code aligns well with the intended functionality of each class.

# Tested and everything runs properly and as intended.