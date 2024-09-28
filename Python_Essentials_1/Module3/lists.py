numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.

numbers[0] = 111
print("\nPrevious list contents:", numbers)  # Printing previous list contents.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list contents:", numbers)  # Printing current list contents.

print("\nList length:", len(numbers))  # Printing the list's length.

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

numbers = [111, 7, 2, 1]
print(numbers[-1]) # Negative indices are legal

numbers.append(4)

print(len(numbers))
print(numbers)


numbers.insert(0, 222)
print(len(numbers))
print(numbers)