# if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% 
# of the income minus 556 thalers and 2 cents (this was what they called tax relief)
# if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, 
# plus 32% of the surplus over 85,528 thalers.

income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
# Write the rest of your code here.
else:
      tax = 14839.02 + (income - 85528) * 0.32

if tax < 0:
    tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")