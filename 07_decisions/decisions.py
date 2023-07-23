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
    print ("a is equal to b")


a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")
    
# 'and' and 'or' operators
a = 23
b = 34

if a == 34 or b == 34:
    print(a + b)
    
if a == 34 and b == 34:
    print (a + b)