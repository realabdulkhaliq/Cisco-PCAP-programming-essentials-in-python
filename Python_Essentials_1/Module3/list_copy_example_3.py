list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
 
del list_1[0]
print(list_2[:]) # By value
del list_2[:]
 
print(list_3)