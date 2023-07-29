class Flower:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (${self.price:.2f}) - Quantity: {self.quantity}"

class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    def __str__(self):
        return "\n".join(str(flower) for flower in self.flowers)

class Inventory:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def get_flower_by_name(self, name):
        for flower in self.flowers:
            if flower.name == name:
                return flower
        return None

    def order_more_flowers(self, name, quantity_to_order):
        flower = self.get_flower_by_name(name)
        if flower:
            flower.quantity += quantity_to_order
        else:
            print(f"{name} is not in the inventory.")

    def need_to_order(self, name, quantity_needed):
        flower = self.get_flower_by_name(name)
        if flower and flower.quantity < quantity_needed:
            return True
        return False
import tkinter as tk
from tkinter import messagebox

class FlowerShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flower Shop Ordering To Go")
        
        self.inventory = Inventory()
        self.initialize_inventory()

        self.bouquet = Bouquet()

        self.create_widgets()

    def initialize_inventory(self):
        # Add flowers to the inventory (you can customize this based on your shop's inventory)
        self.inventory.add_flower(Flower("Rose", 2.99, 10))
        self.inventory.add_flower(Flower("Lily", 3.49, 15))
        self.inventory.add_flower(Flower("Tulip", 1.99, 20))

    def create_widgets(self):
        # GUI elements here (labels, buttons, entry fields, etc.)
        pass

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = FlowerShopApp(root)
    root.mainloop()
