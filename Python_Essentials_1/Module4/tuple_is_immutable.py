#  don't try to modify a tuple's contents! It's not a list!

my_tuple = (1, 10, 100, 1000)

# my_tuple.append(10000)    AttributeError: 'tuple' object has no attribute 'append'
# del my_tuple[0]           TypeError: 'tuple' object doesn't support item deletion
# my_tuple[1] = -10         TypeError: 'tuple' object does not support item assignment