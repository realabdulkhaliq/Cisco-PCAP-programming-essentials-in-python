# if you pass a list to a function, the function has to handle it like a list.

def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

print(list_sum([5, 4, 3]))

# print(list_sum(5)) TypeError: 'int' object is not iterable