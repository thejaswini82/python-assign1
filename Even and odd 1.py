# define the series of numbers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# initialize counters for even and odd numbers
even_count = 0
odd_count = 0

# loop over the numbers in the series
i = 0
while i < len(numbers):
    # check if the number is even
    if numbers[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    i += 1

# output the results
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
