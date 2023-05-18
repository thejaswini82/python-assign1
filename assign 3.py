def sum_list_numbers():
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]
    total = sum(numbers)
    return total

result = sum_list_numbers()
print("Sum of the numbers:", result)

