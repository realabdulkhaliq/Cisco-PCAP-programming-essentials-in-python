def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
    
adding(1, 2, 3)
adding(c = 1, a = 2, b = 3)
adding(3, c = 1, b = 2)

# Look at the invocation below - it seems that we've tried to set a twice:
# adding(3, a = 1, b = 2)
# TypeError: adding() got multiple values for argument 'a'