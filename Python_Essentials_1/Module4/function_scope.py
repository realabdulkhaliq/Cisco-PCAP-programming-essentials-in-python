def scope_test():
    x = 123


scope_test()
# print(x) NameError: name 'x' is not defined

print("====================")

def my_function():
    print("Do I know that variable?", var)

var = 1
my_function()
print(var)

# a variable existing outside a function has scope inside the function's body.

print("====================")
def my_function2():
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function2()
print(var)

# the var variable created inside the function is not the same as when defined outside it ‒ 
# it seems that there two different variables of the same name;
# moreover, the function's variable shadows the variable coming from the outside world.

# NOTE: A variable existing outside a function has scope inside the function's body, 
# excluding those which define a variable of the same name.