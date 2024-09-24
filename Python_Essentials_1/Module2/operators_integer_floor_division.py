print(6 // 3) # Int
print(6 // 3.) # Float
print(6. // 3) # Float
print(6. // 3.) # Float
print(6 // 4) # Int
print(6. // 4) # Float

print("=====")
print(6 // 4) # 6/4 = 1.5 ans is 1
print(-6 // 4) # -6/4 = -1.5 rounding always goes to the lesser integer so ans is 2
print(6. // -4)

# NOTE: The result of the division operator is the integer part of the division 
# (truncated toward zero). rounding always goes to the lesser integer.

print("=======")

print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))