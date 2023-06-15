class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def get_info(self):
        print(f"Coat Color: {self.coat_color}")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def fetch_ball(self):
        print(f"{self.name} is fetching the ball!")

    def bark(self):
        print(f"{self.name} is barking!")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def sleep(self):
        print(f"{self.name} is sleeping zzzz...")

    def drool(self):
        print(f"{self.name} is drooling!")


# Creating objects and implementing the functionalities
dog1 = Dog("Max", 5, "Brown")
dog1.description()  # Output: Name: Max, Age: 5
dog1.get_info()  # Output: Coat Color: Brown

terrier = JackRussellTerrier("Rocky", 3, "White and Brown")
terrier.description()  # Output: Name: Rocky, Age: 3
terrier.get_info()  # Output: Coat Color: White and Brown
terrier.fetch_ball()  # Output: Rocky is fetching the ball!
terrier.bark()  # Output: Rocky is barking!

bulldog = Bulldog("Spike", 4, "Fawn")
bulldog.description()  # Output: Name: Spike, Age: 4
bulldog.get_info()  # Output: Coat Color: Fawn
bulldog.sleep()  # Output: Spike is sleeping zzzz...
bulldog.drool()  # Output: Spike is drooling!
