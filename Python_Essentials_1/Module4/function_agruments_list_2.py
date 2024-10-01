def my_function(my_list_1):
    print("Print #1:", my_list_1) # [2, 3]
    print("Print #2:", my_list_2) # [2, 3]
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1) # [3]
    print("Print #4:", my_list_2) # [3]


my_list_2 = [2, 3]
my_function(my_list_2) # [2, 3] goes to function
print("Print #5:", my_list_2) # [3]