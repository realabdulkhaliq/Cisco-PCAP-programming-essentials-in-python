# blocks = int(input("Enter the number of blocks: "))

# for i in range(1, blocks+1):

#     # if (i * (i + 1)) / 2 >= blocks:
#     #     height = i
#     #     break	

# print("The height of the pyramid:", height)


# def pyramid_height(blocks):
#     height = 0
#     layer = 1

#     while blocks >= layer:
#         blocks -= layer  # Subtract the blocks required for the current layer
#         height += 1  # Increase the height of the pyramid
#         layer += 1  # Move to the next layer, which needs one more block than the current layer

#     return height

# # Example test cases
# blocks = int(input("Enter the number of blocks: "))
# print("The height of the pyramid is:", pyramid_height(blocks))


blocks = int(input("Enter the number of blocks: "))
height = 0
layer = 1

while blocks >= layer:
    blocks -= layer  # Subtract the blocks required for the current layer
    print("blocks",blocks)
    height += 1  # Increase the height of the pyramid
    print("height",height)
    layer += 1  # Move to the next layer, which needs one more block than the current layer
    print("layer",layer)

    
# Example test cases
print("The height of the pyramid is:", height)
