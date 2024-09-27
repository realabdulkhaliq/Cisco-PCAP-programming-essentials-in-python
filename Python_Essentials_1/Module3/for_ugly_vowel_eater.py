# Prompt the user to enter a word
user_word = input("Enter a word: ")
# and assign it to the user_word variable.

for letter in user_word:
    # Complete the body of the for loop.
    if letter.upper() == 'A' or letter.upper() == 'E' or letter.upper() == 'I' or letter.upper() == 'O' or letter.upper() == 'U':
        continue
    else:
        print(letter.upper())

