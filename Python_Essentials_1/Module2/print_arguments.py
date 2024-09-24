# multiple arguments
print("The itsy bitsy spider" , "climbed up" , "the waterspout.") # The arguments are separated by commas.

# the print() function puts a space between the outputted arguments on its own initiative.

print("My name is","Python.")

print("Two",2)

# Positional arguments
# The way in which we are passing the arguments into the print() function 
# is the most common in Python, and is called the positional way.

# Keyword arguments
print("My name is", "Python.") # by default end="\n"
print("My name is", "Python.", end=" ")
print("Monty Python.")

# NOTE: any keyword arguments have to be put after the last positional argument

print("My", "name", "is", "Monty", "Python.", sep="-")
# This is used for making URLs

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print("Python")

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
# Due to end="\n"

print("Multiply String" * 3)
print("Multiply String" * 3, sep="-",end="-")