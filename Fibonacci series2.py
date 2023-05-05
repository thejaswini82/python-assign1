# initialize variables for the first two terms
a, b = 0, 1

# loop to generate the next terms
while a <= 50:
    # print the current term if it's between 0 and 50
    if a > 0:
        print(a, end=" ")
    # calculate the next term
    c = a + b
    # update variables for the next iteration
    a, b = b, c
