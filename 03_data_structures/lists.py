from collections import deque

# lists
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]

print(fruits.count("apple"))
print(fruits.count("tangerine"))
print(fruits.index("banana"))
print(fruits.index("banana", 4))  # Find next banana starting a position 4
print(fruits.reverse())

fruits.append("grape")
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
