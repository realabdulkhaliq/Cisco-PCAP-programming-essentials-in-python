var = 2
print(var)    # outputs: 2

def return_var():
    global var
    var = 5
    return var

print(return_var())    # outputs: 5
print(var)    # outputs: 5