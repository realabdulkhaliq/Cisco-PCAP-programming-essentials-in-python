sum = 0
for i in range(1, 6):
    number = int(input("Enter number: "))
    sum += number
    
print("The sum of the numbers is", sum)
percentage = (sum / 500) * 100
print("The percentage of the numbers is", percentage)
if percentage >= 33:
    print("You're Pass")
else:
    print("You're Fail")