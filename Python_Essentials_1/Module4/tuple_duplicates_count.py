tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    # outputs: 4

# Convert list to tuple
my_list = ["car", "Ford", "flower", "Tulip"]

t = tuple(my_list)
print(t)

# Convert tuple to dictionary
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)