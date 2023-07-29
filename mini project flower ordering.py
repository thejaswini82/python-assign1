class Flower:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price} per stem"

class Bouquet:
    def __init__(self, name):
        self.name = name
        self.flowers = []

    def add_flower(self, flower, quantity):
        if quantity > flower.quantity:
            print(f"Not enough {flower.name} in stock.")
            return
        flower.quantity -= quantity
        self.flowers.append((flower, quantity))

    def get_total_price(self):
        total_price = 0
        for flower, quantity in self.flowers:
            total_price += flower.price * quantity
        return total_price

    def __str__(self):
        bouquet_str = f"Bouquet: {self.name}\n"
        for flower, quantity in self.flowers:
            bouquet_str += f"{flower.name} - {quantity} stems\n"
        bouquet_str += f"Total Price: ${self.get_total_price():.2f}\n"
        return bouquet_str

if __name__ == "__main__":
    # Sample Flowers
    rose = Flower("Rose", 2.5, 20)
    tulip = Flower("Tulip", 1.8, 15)
    lily = Flower("Lily", 3.0, 18)

    flowers = [rose, tulip, lily]

    # Flower Inventory
    flower_inventory = {}
    for flower in flowers:
        flower_inventory[flower.name] = flower

    # Flower Shop Application
    print("Welcome to the Flower Shop Ordering To Go!")
    while True:
        print("\nMenu:")
        print("1. Create a Bouquet")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            bouquet_name = input("Enter the name of the bouquet: ")
            bouquet = Bouquet(bouquet_name)

            print("\nAvailable Flowers:")
            for flower in flowers:
                print(flower)

            while True:
                flower_name = input("\nEnter the name of the flower to add (or 'done' to finish): ")
                if flower_name.lower() == "done":
                    break

                if flower_name not in flower_inventory:
                    print("Invalid flower name.")
                    continue

                flower = flower_inventory[flower_name]
                quantity = int(input(f"Enter the number of {flower.name} stems to add: "))

                bouquet.add_flower(flower, quantity)

            print("\nYour Bouquet:")
            print(bouquet)

        elif choice == "2":
            print("Thank you for using the Flower Shop Ordering To Go!")
            break

        else:
            print("Invalid choice. Please try again.")
