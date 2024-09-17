print(123)
print("abc")

#
#           print(123abc)
#           Cell In[2],   line 1
#           print(123abc)
#                    ^
#           SyntaxError: invalid decimal literal
#

print(123, "abc")   # This is correct


print("My", "name", "is", "Monty", "Python.", sep="-")
# This can be used for creating website urls


print("Programming","Essentials","in", sep="***", end="...")
print("Python")
