def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")

happy_new_year()

print("Invoke Again with False Argument")

happy_new_year(False)