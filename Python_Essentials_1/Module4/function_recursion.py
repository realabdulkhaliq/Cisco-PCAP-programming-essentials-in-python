def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)

print(fun(25))

# Let's break down the execution of fun(25):
# First call: fun(25):
# 25 is not greater than 30, so it returns 25 + fun(28).

# Second call: fun(28):
# 28 is not greater than 30, so it returns 28 + fun(31).

# Third call: fun(31):
# 31 is greater than 30, so it returns 3 (this is the base case).

# Now let's substitute the results back into the original calls:
# The third call returns 3, so the second call becomes 28 + 3 = 31.
# The second call returns 31, so the first call becomes 25 + 31 = 56.

# 25 + 28 + 3 = 56, which is the final result.