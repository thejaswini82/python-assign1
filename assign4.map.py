# Input list
numbers = input("Enter a list of integers (comma-separated): ").split(",")
numbers = [int(num) for num in numbers]

# Triple function using lambda
triple = lambda x: x * 3

# Apply map function to triple each element in the list
result = list(map(triple, numbers))

print("Triple of list numbers:")
print(result)

