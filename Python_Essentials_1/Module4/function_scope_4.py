a = 1

def fun():
    global a
    a = 2
    print(a)

fun() # Output 2
print(a) # Output 2
a = 3
print(a) # Output 3