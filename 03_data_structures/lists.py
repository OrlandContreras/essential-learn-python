from collections import deque

# lists
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]

print(fruits.count("apple"))
print(fruits.count("tangerine"))
print(fruits.index("banana"))
print(fruits.index("banana", 4))  # Find next banana starting a position 4
print(fruits.reverse())

# Add items to a list
fruits.append("grape")
print(fruits)

fruits.insert(1, "mango")  # insert at a given position
print(fruits)

fruits.sort()
print(fruits)

fruits.pop()
print(fruits)

# Using Lists as Stacks
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

# Using Lists as Queues
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())  # The first to arrive now leaves
print(queue.popleft())  # The second to arrive now leaves
print(queue)  # Remaining queue in order of arrival

# Sets
basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(basket)  # show that duplicates have been removed

# Demonstrate set operations on unique letters from two words
a = set("abracadabra")
b = set("alacazam")

print(a)  # unique letters in a
print(a - b)  # letters in a but not in b
print(a | b)  # letters in a or b or both
print(a & b)  # letters in both a and b
print(a ^ b)  # letters in a or b but not both

# Sorting a list
my_list = [3, 5, 1, 2, 4]

for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] > my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]

print(my_list)

# Working with slices
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_1)
print(list_2)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# Negative slices
my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:-3:-1]
print(new_list)

# del instruction
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)
