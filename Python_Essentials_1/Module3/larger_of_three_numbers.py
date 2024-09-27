number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if number1 > number2:
    larger_number = number1
    if larger_number > number3:
        print("The larger number is:", larger_number)
    else:
        print("The larger number is:", number3)
else:
    larger_number = number2
    if larger_number > number3:
        print("The larger number is:", larger_number)
    else:
        print("The larger number is:", number3)