def count_upper_lower():
    string = input("Enter a string: ")
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

result = count_upper_lower()
print("No. of Upper case characters:", result[0])
print("No. of Lower case characters:", result[1])

