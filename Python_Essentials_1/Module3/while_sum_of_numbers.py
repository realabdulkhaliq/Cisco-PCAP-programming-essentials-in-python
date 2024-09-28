number = int(input("Enter a number or 0 for Exit: "))
sum = 0
while number != 0:
    sum += number
    number = int(input("Enter a number or 0 for Exit: "))

print("Sum of numbers is: ", sum)