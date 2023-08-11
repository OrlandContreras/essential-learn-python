"""
The scope of a name (e.g., a variable name) is the part of a code where the name is properly recognizable.

For example, the scope of a function's parameter is the function itself. 
The parameter is inaccessible outside the function.
"""


# a variable existing outside a function has scope inside the function's body.
def my_function():
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)


# A variable existing outside a function has scope inside the function's body,
# excluding those which define a variable of the same name.
def my_function_2():
    var2 = 2
    print("Do I know that variable?", var2)


var2 = 1
my_function_2()
print(var2)


# The global keyword allows you to modify the variable outside of the current scope.
# It is used to create a global variable and make changes to the variable in a local context.
# Use of the global keyword outside a function has no effect.
def my_function_3():
    global var3
    var3 = 3
    print("Do I know that variable?", var3)


var3 = 1
my_function_3()
print(var3)


# Function interaction with arguments
def another_function(n):
    print("I got", n)
    n += 1
    print("I have", n)


var4 = 1
another_function(var4)
print(var4)


# Sample functions: Evaluating the BMI
# BMI = weight / height^2
# weight in kg, height in m
def bmi(weight, height):
    return weight / height**2


print(bmi(52.5, 1.65))


# Evaluating BMI and converting imperial units to metric units
def bmi_2(weight, height, system="metric"):
    """
    This function calculates the BMI and converts the units if necessary.
    """
    if system == "metric":
        return weight / height**2
    elif system == "imperial":
        return 703 * weight / height**2
    else:
        print("Please use metric or imperial as system.")
        return None


print(bmi_2(352.5, 1.65))


# Sample functions: Triangles
# A triangle is a polygon with three edges and three vertices.
# It is one of the basic shapes in geometry.
# A triangle with vertices A, B, and C is denoted triangle ABC.
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


# Recursion
# Recursion is a very important concept in functional programming.
# The recursive call may be the last action in the function.
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


for n in range(1, 10):
    print(n, "->", fib(n))
