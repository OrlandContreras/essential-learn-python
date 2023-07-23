# Example input function
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

# Example input function with an argument
anything_again = input("Tell me anything... ")
print("Hmm...", anything_again, "... Really?")

# This means that you mustn't use it as an argument of any arithmetic operation.
'''
anything = input("Enter a number: ")
something = anything ** 2.0 # TypeError
print(anything, "to the power of 2 is", something)

'''

# Type casting
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypotenuse = (leg_a ** 2 + leg_b ** 2) ** .5
print("Hypotenuse length is", hypotenuse)
print("Hyponetus length is", (leg_a ** 2 + leg_b ** 2) ** .5) # Remove the variable hypotenuse

# String operators
# Concatenation
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

# Repetition
print("Hip "*2 + "Hooray!")
print("Hip "*2 + "Hooray" + "!"*10)
print(("Hip "*2 + "Hooray" + "!"*10)*3)

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")