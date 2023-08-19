# Working with print() function
print("Hello, Python!")

# Add escape and newline characters
print("\nThe itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain \nand washed the spider out.")

# Using multiple arguments
print("\nthe itsy bitsy spider", "climbed up", "the waterspout")

# Using keyword arguments
print("\nMy name is", "Python.", end=" ")
print("Monty Python.")

print("\nMy", "name", "is", "Python", sep="-")

print("\nMy", "name", "is", sep="_", end="*")
print("Monty", "Python", sep="*", end="*\n")

# Example. Expected output:
# Programming***Essentials***in...Python
print("Programming", "Essentials", "in", "Python", sep="***", end="...")
