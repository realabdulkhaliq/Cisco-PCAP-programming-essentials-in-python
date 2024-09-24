# NOTE: PEMDAS

# PRIORITY: (), ** , +/- (unary), *, /, //, %, +/- (binary)

print(2 * 3 % 5)
print(2 * (3 % 5))

print("=====")
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2) # Ans in float due to one division
print((5 * ((25 % 13) + 100) // (2 * 13)) // 2) # Now ans in int