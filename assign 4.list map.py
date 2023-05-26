numbers = input("Enter a list of numbers, separated by commas: ").split(",")
numbers = list(map(int, numbers))

squared_numbers = list(map(lambda x: x ** 2, numbers))

print("Square of list numbers:")
print(squared_numbers)
