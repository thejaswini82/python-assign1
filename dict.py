#1way
#dictionary = {}
#for i in range(97, 123):
 #   dictionary[chr(i)] = i
#print(dictionary)

#2way
# Create an empty dictionary
ascii_dict = {}

# Iterate over the range of ASCII values for a-z (97-122)
for ascii_value in range(97, 123):
    # Use chr() function to get the character corresponding to the ASCII value
    character = chr(ascii_value)
    # Add the key-value pair to the dictionary
    ascii_dict[character] = ascii_value

# Print the resulting dictionary
print(ascii_dict)
