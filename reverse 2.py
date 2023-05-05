# get the word from the user
word = input("Enter a word: ")

reversed_word = ""

# loop over the characters in the word in reverse order
i = len(word) - 1
while i >= 0:
# add the current character to the reversed word
    reversed_word += word[i]
    i -= 1
print("Reversed word:", reversed_word)
