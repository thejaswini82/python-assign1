
string = input("Enter a string: ")

# Convert the string to lowercase using the lower() method
string = string.lower()

# Define an empty dictionary
ascii_dict = {}

# Use a loop to iterate over the lowercase letters a-z
for char in range(ord('a'), ord('z')+1):
    # Convert the ASCII value back to the corresponding character using chr() function, and use it as the key
    # Add the key-value pair to the dictionary
    ascii_dict[chr(char)] = char

# Use a loop to iterate over the characters in the lowercase string
for char in string:
    # Check if the character is a lowercase letter
    if char.islower():
        # Print the key-value pair corresponding to the character
        print(char, ":", ascii_dict[char])


