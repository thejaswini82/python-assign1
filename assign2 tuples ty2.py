# Get the list of tuples as input from the user
n = int(input("Enter number of tuples: "))
tuples = []

for i in range(n):
    tuple_elements = list(map(int, input("Enter tuple elements separated by space: ").strip().split()))
    tuples.append(tuple(tuple_elements))

# Define a function to extract the last element of each tuple
def last_element(t):
    return t[-1]

# Use the sorted() function to sort the list based on the last element of each tuple
sorted_tuples = sorted(tuples, key=last_element)

# Print the sorted list
print("Sorted list of tuples:", sorted_tuples)
