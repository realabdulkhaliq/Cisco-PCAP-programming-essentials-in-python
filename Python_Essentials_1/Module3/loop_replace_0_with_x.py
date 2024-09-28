# Create a program with a for loop and a continue statement. 
# The program should iterate over a string of digits, replace each 0 with x, 
# and print the modified string to the screen.
new_string = ""

for digit in "0165031806510":
    if digit == "0":
        # Line of code.
        new_string += "x"
        # Line of code.
    else:
        new_string += digit
    # Line of code.
print(new_string)