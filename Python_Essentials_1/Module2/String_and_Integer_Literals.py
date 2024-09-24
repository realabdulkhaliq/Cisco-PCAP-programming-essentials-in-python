# A literal is data whose values are determined by the literal itself.
print("2")
print(2)

print(2)
print(2+2)
print(2.2)

# *integers*, that is, those which are devoid of the fractional part;
# and *floating-point* numbers (or simply floats), that contain (or are able to contain) the fractional part.
# The characteristic of the numeric value which determines its kind, range, and application, is called the type.
print(type(2))

#! print(11 11 11) It's prohibited.

# Python does allow, though, is the use of underscores in numeric literals.
print(11_111_111) # Output 11111111
print(11_111_111.11) # Output 11111111.11
print(-11_111_111) # Negative Number

# There is one more, special literal that is used in Python: the None literal. 
# This literal is a NoneType object, and it is used to represent the absence of a value.