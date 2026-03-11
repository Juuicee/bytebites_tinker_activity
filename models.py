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
    def add_order(self, order):
        """
        Add an Order to this customer's purchase history.
        """
        self.purchase_history.append(order) # Added by copilot and it works as intended.

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
    def add_item(self, item: FoodItem):
        """
        Add a FoodItem to the menu.
        """
        self.items.append(item) # Added by copilot and it works as intended.

    def filter_by_category(self, category: str):
        """
        Return a list of FoodItems in this menu that match the given category.
        """
        return [item for item in self.items if item.category == category] # Added by copilot and it works as intended.

class Order:
    # Initialize an order with a customer and an empty list of selected items. Copilot generated the rest of the code based on the provided context.
    def __init__(self, customer):
        self.items = []
        self.customer = customer
    def add_item(self, item: FoodItem):
        """
        Add a FoodItem to this order.
        """
        self.items.append(item) # Added by copilot and it works as intended.

    def calculate_total(self) -> float:
        """
        Calculate and return the total price of all items in this order.
        """
        return sum(item.price for item in self.items) # Added by copilot and it works as intended.


# Copilot matched my design choices!
# Copilot reviewed one class at a time and suggested methods for adding items to the menu, filtering items by category, adding items to an order, and calculating the total cost of an order. The generated code aligns well with the intended functionality of each class.

# Tested and everything runs properly and as intended.



# Created scenario to test the functionality of the classes and methods. The scenario includes creating food items, adding them to a menu, filtering items by category, creating a customer, placing an order, and calculating the total cost of the order. 
# The output matches the expected results based on the provided context.

# Used copilot to generate test scenarios.
if __name__ == "__main__":
    # --- Create some FoodItem objects ---
    burger = FoodItem("Spicy Burger", 10.0, "Main", 5)
    soda = FoodItem("Large Soda", 3.0, "Drink", 7)
    ice_cream = FoodItem("Vanilla Ice Cream", 4.5, "Dessert", 8)
    fries = FoodItem("French Fries", 2.5, "Snack", 6)

    # --- Create a Menu and add items ---
    menu = Menu()
    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(ice_cream)
    menu.add_item(fries)

    # --- Test filtering by category ---
    drinks = menu.filter_by_category("Drink")
    print("Filtered Drinks:", [item.name for item in drinks])  # Expect: ["Large Soda"]

    desserts = menu.filter_by_category("Dessert")
    print("Filtered Desserts:", [item.name for item in desserts])  # Expect: ["Vanilla Ice Cream"]

    # --- Create a Customer ---
    alice = Customer("Alice")

    # --- Create an Order for Alice and add items ---
    order1 = Order(alice)
    order1.add_item(burger)
    order1.add_item(fries)
    order1.add_item(soda)

    # --- Add order to customer's purchase history ---
    alice.add_order(order1)

    # --- Calculate total for Alice's order ---
    print(f"Order total for {alice.name}: ${order1.calculate_total():.2f}")  # Expect: 10 + 2.5 + 3 = 15.5

    # --- Print customer purchase history summary ---
    for i, order in enumerate(alice.purchase_history, start=1):
        print(f"Order {i} items:", [item.name for item in order.items])