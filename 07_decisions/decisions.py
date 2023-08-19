# Explain how you can use a conditional statement:
# Single statement
x = 10

if x == 10:  # condition
    print("x is equal to 10")  # Executed if the condition is True.

# Multiple statements
x = 10

if x > 5:  # condition one
    print("x is greater than 5")  # Executed if condition one is True.

if x < 10:  # condition two
    print("x is less than 10")  # Executed if condition two is True.

if x == 10:  # condition three
    print("x is equal to 10")  # Executed if condition three is True.

# Use if-else:
x = 10

if x < 10:  # Condition
    print("x is less than 10")  # Executed if the condition is True.

else:
    print("x is greater than or equal to 10")  # Executed if the condition is False.


# A series of if statements followed by an else statement:
x = 10

if x > 5:  # True
    print("x > 5")

if x > 8:  # True
    print("x > 8")

if x > 10:  # False
    print("x > 10")

else:
    print("else will be executed")

# The if-elif-else statement:
x = 10

if x == 10:  # True
    print("x == 10")

if x > 15:  # False
    print("x > 15")

elif x > 10:  # False
    print("x > 10")

elif x > 5:  # True
    print("x > 5")

else:
    print("else will not be executed")

# Nested conditional statements:
x = 10

if x > 5:  # True
    if x == 6:  # False
        print("nested: x == 6")
    elif x == 10:  # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")


# Other examples:
x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
print((y - 5) == x)

# Read two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Choose the larger number
if num1 > num2:
    larger_number = num1
else:
    larger_number = num2

# Print the result
print("The larger number is:", larger_number)

# Work with elif
a = 27
b = 93
if a <= b:
    print("a is less than or equal to b")
elif a == b:
    print("a is equal to b")

# Work with if, else and elif
if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b")


a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print("a is greater than b and b is greater than c")
    else:
        print("a is greater than b and less than c")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")

# 'and' and 'or' operators
a = 23
b = 34

if a == 34 or b == 34:
    print(a + b)

if a == 34 and b == 34:
    print(a + b)
