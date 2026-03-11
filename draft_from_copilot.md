class Customer {
  - name: String
  - purchaseHistory: List<Order>
  + getName(): String
  + addOrder(order: Order): void
  + getPurchaseHistory(): List<Order>
}

class FoodItem {
  - name: String
  - price: double
  - category: String
  - popularityRating: int
  + getName(): String
  + getPrice(): double
  + getCategory(): String
  + getPopularityRating(): int
}

class Menu {
  - items: List<FoodItem>
  + addItem(item: FoodItem): void
  + filterByCategory(category: String): List<FoodItem>
  + sortByPopularity(): List<FoodItem>
}

class Order {
  - customer: Customer
  - items: List<FoodItem>
  + addItem(item: FoodItem): void
  + calculateTotal(): double
}

Customer --> Order : has purchaseHistory (1..*)
Menu --> FoodItem : contains (1..*)
Order --> FoodItem : contains (1..*)
Order --> Customer : belongs to (1)