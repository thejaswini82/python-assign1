# define the series of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# count the number of even and odd numbers using a list comprehension and the sum() function
even_count = sum(1 for n in numbers if n % 2 == 0)
odd_count = sum(1 for n in numbers if n % 2 != 0)
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
