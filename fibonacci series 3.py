# prompt user for the number of terms to generate
n = int(input("Enter the number of terms: "))

# initialize variables for the first two terms
a, b = 1, 1

# print the first two terms
print(a, end=" ")
print(b, end=" ")

# loop to generate the remaining terms
for i in range(2, n):
    # calculate the next term
    c = a + b
    # print the next term
    print(c, end=" ")
    # update variables for the next iteration
    a, b = b, c

#enter an input number 9 then
    #output:1 1 2 3 5 8 13 21 34
    
