# Write a program which reads the number of blocks the builders have, 
# and outputs the height of the pyramid that can be built using these blocks.
blocks = int(input("Enter the number of blocks: "))

for height in range(1, blocks + 1):
    blocks -= height
    if blocks < 0:
        break
    else:
        height += 1
print("The height of the pyramid:", height - 1)