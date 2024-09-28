i = 0
while i <= 3 :
    i += 2
    print("*")

print("===========")

i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
      break
    print("*")

print("===========")

for i in range(1):
    print("#")
else:
    print("#")

print("===========")

var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")

print("===========")

var = 1
while var < 10:
    print("#")
    var = var << 1

print("===========")

z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)

print("===========")

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
 
print(c + d + e)

print("===========")

my_list = [3, 1, -2]
print(my_list[my_list[-1]])

print("===========")

my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

print("===========")

vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0]

print(vals)

print("===========")

vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]
print(vals)

print("===========")

nums = [1, 2, 3]
vals = nums
del vals[1:2]
print(nums, vals)

print("===========")
nums = [1, 2, 3]
vals = nums[-1:-2]
print(nums, vals)

print("===========")
my_list_1 = [1, 2, 3]
my_list_2: list = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)

print("===========")

my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)
 
print("===========")
my_list = [i for i in range(-1, 2)]
print(my_list)


print("===========")
t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)

print("===========")
# my_list = [[0, 1, 2, 3] for i in range(2)]
# print(my_list[2][0]) Error
# print(my_list)


print(1//2*3)
print(2+3*5.)
my_list = [ 0 for i in range(1,3)]
print(my_list)