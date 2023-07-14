# if Statements
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")

# for Statements
words = ["cat", "window", "defenestrate"]

for w in words:
    print(w, len(w))

users = {
    "Hans": "active",
    "Peter": "inactive",
    "Klaus": "active",
}  # Create a sample collection

# Strategy 1: Iterate over a copy
for user, status in users.copy().items():
    if status == "inactive":
        del users[user]

# Strategy 2: Create a new collection
active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = status

print(users)
print(active_users)


# range() Function
for i in range(5):
    print(i)

print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))

a = ["Mary", "had", "a", "little", "lamb"]
for i in range(len(a)):
    print(i, a[i])

print(range(10))
print(sum(range(4)))  # 0 + 1 + 2 + 3

# break and continue Statements, and else Clauses on Loops
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:  # If x divides n without remainder
            print(n, "equals", x, "*", n // x)
            break  # Exit the loop
    else:  # If no break occurred
        # loop fell through without finding a factor
        print(n, "is a prime number")

for num in range(2, 10):
    if num % 2 == 0:  # If the number is even
        print("Found an even number", num)
        continue  # Jump to the next iteration
    print("Found a number", num)


# pass Statements
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)


class MyEmptyClass:
    pass


def initlog(*args):
    pass  # Remember to implement this!


# match Statements (Python 3.10+)
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the Internet"


def match_point(point):
    # point is a tuple (x, y)
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(0, y):
            print(f"Y={y}")
        case Point(x, 0):
            print(f"X={x}")
        case Point(x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")


# Documentation Strings
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass


print(my_function.__doc__)
