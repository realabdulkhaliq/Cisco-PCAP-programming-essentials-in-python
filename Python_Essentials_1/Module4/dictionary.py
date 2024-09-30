dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}

empty_dictionary: dict = {} # empty dictionary
# The empty dictionary is constructed by an empty pair of curly braces − nothing unusual.

print(dictionary)
print(phone_numbers)
print(empty_dictionary)
print(dictionary['cat'])


words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")


print("====== Printing Keys =======")
for key in dictionary.keys():
    print(key, "->", dictionary[key])

print("====== Printing Values =======")
for french in dictionary.values():
    print(french)

print("====== Printing Items =======")
for english, french in dictionary.items():
    print(english, "->", french)