print("This is my first program!")

# myName("Ali")   # You can't call any function before decleration
# def myName(name):
#     print("My name is: ", name)

def intro(fn, ln):
    print("I am ", fn, ln)
    return 123

intro("M", "Awais")

# Return didn't print

out = intro("M", "Ali")
print(out)  # Now return 123 print

def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return 123
 
    print("Happy New Year!")

happy_new_year()
happy_new_year(False)
num = happy_new_year()
print(num)
num1 = happy_new_year(False)
print(num1)

