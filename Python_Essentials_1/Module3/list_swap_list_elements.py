my_list = [10, 1, 8, 3, 5]

print("Old list", my_list)

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print("Swaped list",my_list)