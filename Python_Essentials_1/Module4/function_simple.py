def message():
    print("Enter a value: ")
 
print("We start here.")
message()
print("We end here.")

# It's legal, and possible, to have a variable named the same as a function's parameter.

def message1(number):
    print("Enter a number:", number)

number = 1234
message1(1)
print(number)

# A situation like this activates a mechanism called shadowing:
# parameter number shadows any variable of the same name