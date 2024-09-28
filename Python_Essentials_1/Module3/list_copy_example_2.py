list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

print("list 1",list_1)
print("list 2",list_2)
print("list 3",list_3)

del list_1[0]
print("list 2",list_2)
del list_2
 
print("list 1",list_1)
# print(list_2) Error because not exist
print("list 3",list_3)