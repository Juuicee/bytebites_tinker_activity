import pytest

from models import Customer, FoodItem, Menu, Order

# --- Test 1: Order total with multiple items (Happy Path) ---
def test_calculate_total_with_multiple_items():
    # Setup
    customer = Customer("Bob")
    burger = FoodItem("Burger", 10.0, "Main", 5)
    soda = FoodItem("Soda", 5.0, "Drink", 7)
    order = Order(customer)
    order.add_item(burger)
    order.add_item(soda)

    # Exercise & Verify
    assert order.calculate_total() == 15.0

# --- Test 2: Order total is zero when order is empty (Edge Case) ---
def test_order_total_is_zero_when_empty():
    customer = Customer("Alfredo")
    order = Order(customer)

    assert order.calculate_total() == 0.0

# --- Test 3: Filtering menu items by category ---
def test_filter_menu_by_category():
    burger = FoodItem("Burger", 10.0, "Main", 5)
    soda = FoodItem("Soda", 5.0, "Drink", 7)
    ice_cream = FoodItem("Ice Cream", 4.0, "Dessert", 8)

    menu = Menu()
    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(ice_cream)

    drinks = menu.filter_by_category("Drink")
    mains = menu.filter_by_category("Main")
    desserts = menu.filter_by_category("Dessert")

    # Verify filtering works
    assert [item.name for item in drinks] == ["Soda"]
    assert [item.name for item in mains] == ["Burger"]
    assert [item.name for item in desserts] == ["Ice Cream"]

    # All tests ran properly and the expected outputs were correct based on the provided context.

