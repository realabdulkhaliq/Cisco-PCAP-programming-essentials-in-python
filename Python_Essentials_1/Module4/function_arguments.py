def my_function(n):
    print("I got", n)
    n += 1      # changing the parameter's value doesn't propagate outside the function
    print("I have", n)


var = 1
my_function(var)
print(var)