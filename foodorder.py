# Class to represent a food item
class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

# Class to represent the restaurant's menu
class Menu:
    def __init__(self):
        self.food_items = []
        
    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = len(self.food_items) + 1
        food_item = FoodItem(food_id, name, quantity, price, discount, stock)
        self.food_items.append(food_item)
        print("Food item added successfully!")
        
    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print("Food item edited successfully!")
                return
        print("Food item not found.")
        
    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                print("Food item removed successfully!")
                return
        print("Food item not found.")
        
    def view_food_items(self):
        for food_item in self.food_items:
            print(f"Food ID: {food_item.food_id}")
            print(f"Name: {food_item.name}")
            print(f"Quantity: {food_item.quantity}")
            print(f"Price: {food_item.price}")
            print(f"Discount: {food_item.discount}")
            print(f"Stock: {food_item.stock}")
            print("-----------------------------")
            
# Class to represent a user
class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []
        
    def place_order(self, menu, food_item_ids):
        order_items = []
        total_price = 0
        
        for food_item_id in food_item_ids:
            for food_item in menu.food_items:
                if food_item.food_id == food_item_id:
                    order_items.append(food_item)
                    total_price += food_item.price
                    break
        
        order = {
            "items": order_items,
            "total_price": total_price
        }
        
        self.orders.append(order)
        print("Order placed successfully!")
        
    def view_order_history(self):
        if len(self.orders) == 0:
            print("No order history found.")
        else:
            for i, order in enumerate(self.orders):
                print(f"Order {i+1}:")
                for food_item in order["items"]:
                    print(f"Food ID: {food_item.food_id}")
                    print(f"Name: {food_item.name}")
                    print(f"Quantity: {food_item.quantity}")
                    print(f"Price: {food_item.price}")
                    print("-----------------------------")
                print(f"Total Price: {order['total_price']}")
                print("=============================")
            
    def update_profile(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        print("Profile updated successfully!")

# Creating an instance of the Menu class
menu = Menu()

# Creating some food items and adding them to the menu
menu.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 10)
menu.add_food_item("Vegan Burger", "1 piece", 320, 0, 5)
menu.add_food_item("Truffle Cake", "500gm", 900, 0, 3)

# Creating an instance of the User class
user = User("Akash", "1234567890", "akash@example.com", "123 Main St", "password")

# Placing an order
user.place_order(menu, [2, 3])

# Viewing order history
user.view_order_history()

# Updating user profile
user.update_profile("Ankith", "9876543210", "ankith.jn@example.com", "456 Elm St", "newpassword")
