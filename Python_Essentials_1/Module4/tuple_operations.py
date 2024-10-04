my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2)) # 9
print(t1) # (1, 10, 100, 1000, 10000)
print(t2) # (1, 10, 100, 1, 10, 100, 1, 10, 100)

print(10 in t2) # True
print(10 in my_tuple) # True
print(-10 not in my_tuple) # True
print(my_tuple[1]) # 10


print("========")
var = 123

a1 = (1, )
a2 = (2, )
a3 = (3, var)

# a1, a2, a3 = a2, a3, a1 This is OK - remove comment and check
 
print(a1, a2, a3)