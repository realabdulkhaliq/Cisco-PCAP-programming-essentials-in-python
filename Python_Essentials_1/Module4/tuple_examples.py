tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)

print("Empty Tuple")
empty_tuple = ()
print(empty_tuple)

# Tuples with one element
# If you want to create a tuple with a single element, you need to include a comma after the 
# element
# Otherwise, Python will not recognize it as a tuple
# This is a common mistake when working with tuples
# The correct way to create a tuple with a single element is to add a comma after the element

# Correct way to create a tuple with a single element
one_element_tuple_1 = (1)
one_element_tuple_2 = (1, )
one_element_tuple_3 = 1.,

print("Access tuple values")
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem, end=",")