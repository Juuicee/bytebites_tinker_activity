@startuml ByteBites UML Diagram
class Customer {
  + name: str
  + purchase_history: list[Order]
  + __init__(name: str)
  + add_order(order: Order)
}

class FoodItem {
  + name: str
  + price: float
  + category: str
  + popularity: int
  + __init__(name: str, price: float, category: str, popularity: int)
}

class Menu {
  + items: list[FoodItem]
  + __init__()
  + add_item(item: FoodItem)
  + filter_by_category(category: str): list[FoodItem]
}

class Order {
  + items: list[FoodItem]
  + customer: Customer
  + __init__(customer: Customer)
  + add_item(item: FoodItem)
  + calculate_total(): float
}

Customer "1" -- "*" Order : purchase_history
Menu "1" -- "*" FoodItem : contains
Order "1" -- "*" FoodItem : selected
@enduml