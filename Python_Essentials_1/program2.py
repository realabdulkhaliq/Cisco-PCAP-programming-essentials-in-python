a = 1

print(a)

def fun():
    global a
    a = 2
    print(a)


a = 3

print(a)
fun()
print(a)