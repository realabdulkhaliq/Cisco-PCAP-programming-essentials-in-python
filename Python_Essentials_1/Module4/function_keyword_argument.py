def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

print("==========")

def new_introduction(first_name, last_name="Smith"): # default (predefined) values
     print("Hello, my name is", first_name, last_name)

new_introduction("John")
new_introduction("James", "Doe") # replaces default value
new_introduction("Henry")
new_introduction(first_name="William")



