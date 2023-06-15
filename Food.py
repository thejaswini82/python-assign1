import random

# FoodItem class to represent a food item
class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = random.randint(1000, 9999)  # Generate a random FoodID
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

# Admin class with functionalities to manage food items
class Admin:
    food_items = []

    @classmethod
    def add_food_item(cls, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        cls.food_items.append(food_item)

    @classmethod
    def edit_food_item(cls, food_id, name, quantity, price, discount, stock):
        for food_item in cls.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                break

    @classmethod
    def view_food_items(cls):
        for food_item in cls.food_items:
            print("FoodID:", food_item.food_id)
            print("Name:", food_item.name)
            print("Quantity:", food_item.quantity)
            print("Price:", food_item.price)
            print("Discount:", food_item.discount)
            print("Stock:", food_item.stock)
            print("")

    @classmethod
    def remove_food_item(cls, food_id):
        for food_item in cls.food_items:
            if food_item.food_id == food_id:
                cls.food_items.remove(food_item)
                break

# User class with functionalities for user operations
class User:
    users = []

    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []

    @classmethod
    def register(cls, full_name, phone_number, email, address, password):
        user = User(full_name, phone_number, email, address, password)
        cls.users.append(user)

    @classmethod
    def login(cls, email, password):
        for user in cls.users:
            if user.email == email and user.password == password:
                return user
        return None

    def place_order(self, food_items):
        order = []
        total_price = 0

        for index in food_items:
            food_item = Admin.food_items[index - 1]
            order.append(food_item)
            total_price += food_item.price

        self.order_history.append(order)
        return total_price

    def view_order_history(self):
        for index, order in enumerate(self.order_history):
            print("Order", index + 1)
            for food_item in order:
                print("FoodID:", food_item.food_id)
                print("Name:", food_item.name)
                print("Quantity:", food_item.quantity)
                print("Price:", food_item.price)
                print("Discount:", food_item.discount)
                print("Stock:", food_item.stock)
                print("")
            print("")

    def update_profile(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

# Sample usage of the Food Ordering app

# Admin functionalities
Admin.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 10)
Admin.add_food_item("Vegan Burger", "1 piece", 320, 10, 5)
Admin.add_food_item("Truffle Cake", "500gm", 900, 5, 3)

# User functionalities
User.register("John Doe", "1234567890", "johndoe@example.com", "123 Main St", "password")

# User login
user = User.login("johndoe@example.com", "password")
if user:
    print("User login successful!")
else:
    print("Invalid credentials!")

# Place new order
print("\nPlacing a new order...")
food_items_selected = [2, 3]  # User selects Vegan Burger and Truffle Cake
total_price = user.place_order(food_items_selected)
print("Order placed successfully!")
print("Total price:", total_price)

# View order history
print("\nOrder history:")
user.view_order_history()

# Update profile
print("\nUpdating profile...")
user.update_profile("Ankith", "1234567890", "ankith.jn@example.com", "456 Elm St", "newpassword")
print("Profile updated successfully!")

