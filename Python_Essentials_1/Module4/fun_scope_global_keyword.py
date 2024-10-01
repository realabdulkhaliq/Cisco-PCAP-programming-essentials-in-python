# There's a special Python method which can extend a variable's scope in a 
# way which includes the function's body

def my_function():
    global var # this var is now everywhere
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)