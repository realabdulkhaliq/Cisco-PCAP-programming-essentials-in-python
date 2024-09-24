# Octal and hexadecimal numbers
# If an integer number is preceded by an 0O or 0o prefix (zero-o), it is octal value.
print(0o123)

# *hexadecimal numbers*. Such numbers should be preceded by the prefix 0x or 0X (zero-x).
print(0x123)

print("This is in decimal", 10)

print("Convert binary to decimal", 0b1010)
print("Convert binary to decimal", 0b1011)
print("==================")
print("Convert octal to decimal", 0o1010)
print("Convert octal to decimal", 0o10)
print("==================")
print("Convert hexa to decimal", 0x1010)
print("Convert hexa to decimal", 0xA)

# `1011`
# `It's 11, because (2**0) + (2**1) + (2**3) = 11`
print("==================")
print("Convert decimal 10 to binary", bin(10))
print("Convert decimal 10 to hexadecimal", hex(10))
print("Convert decimal 10 to octal", oct(10))