# There are only two kinds of circumstances when None can be safely used:

# when you assign it to a variable (or return it as a function's result)
# when you compare it with a variable to diagnose its internal state.

value = None
if value is None:
    print("Sorry, you don't carry any value")

# NOTE: Don't forget this: if a function doesn't return a certain value using a 
# return expression clause, it is assumed that it implicitly returns None.

print("=======")

def strange_function(n):
    if(n % 2 == 0):
        return True
    
print("Above function return None")

print(strange_function(2))
print(strange_function(1)) # None: because else condition is not defined