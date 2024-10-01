def my_function(my_list_1):
    print("Print #1:", my_list_1) # [2, 3]
    print("Print #2:", my_list_2) # [2, 3]
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1) # [0, 1]
    print("Print #4:", my_list_2) # [2, 3]


my_list_2 = [2, 3]
my_function(my_list_2)  # This list goes to the function
print("Print #5:", my_list_2)  # This list goes to the global scope [2, 3]