# define the number as a string
num_str = "123456789"

# initialize counters for even and odd digits
even_count = 0
odd_count = 0

# loop over the digits in the number
for digit in num_str:
    # check if the digit is even
    if int(digit) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# output the results
print("Number of even digits:", even_count)
print("Number of odd digits:", odd_count)
