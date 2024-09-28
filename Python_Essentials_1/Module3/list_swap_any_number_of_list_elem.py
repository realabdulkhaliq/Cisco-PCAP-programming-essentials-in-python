my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print("Old: ",my_list)

for i in range(len(my_list) // 2):
    print(my_list[i])
    
    print(my_list[len(my_list) - i - 1])
    my_list[i], my_list[len(my_list) - i - 1] = my_list[len(my_list) - i - 1], my_list[i]
    # 0         ,       [20 - 0 - 1 = 19]     =         [20 - 0 - 1 = 19],      0         : Index
    # 1         ,           20                =             20          ,       1         : Values
print("New: ", my_list)