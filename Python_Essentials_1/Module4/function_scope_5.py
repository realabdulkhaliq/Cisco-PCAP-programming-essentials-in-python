a = 1

def fun():
    global a
    a = 2
    print(a)

a = 3
print(a) # 3
fun() # 2
print(a) # 2