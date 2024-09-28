# Ex. 1
def subtra(a, b):
    print(a - b)

subtra(5, 2)    # outputs: 3
subtra(2, 5)    # outputs: -3


# Ex. 2

subtra(a=5, b=2)    # outputs: 3
subtra(b=2, a=5)    # outputs: 3

# Ex. 3

subtra(5, b=2)    # outputs: 3
subtra(5, 2)    # outputs: 3

# Ex. 4

# subtra(a=5, 2)    # SyntaxError: positional argument follows keyword argument
# subtra(5, a=2)    # TypeError: subtra() got multiple values for argument 'a'