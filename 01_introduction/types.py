# Numbers
print(1 + 1)  # addition
print(50 - 5 * 6)  # multiplication and subtraction
print((50 - 5 * 6) / 4)  # division always returns a floating point number
print(8 / 5)  # division always returns a floating point number
print(17 / 3)  # division always returns a floating point number
print(17 // 3)  # floor division discards the fractional part
print(-17 // 3)
print(17 % 3)  # the % operator returns the remainder (module) of the division
print(5 * 3 + 2)  # result * divisor + remainder
print(5**2)  # 5 squared
print(2**7)  # 2 to the power of 7
# print(n) # try to access an undefined variable

tax = 12.5 / 100
price = 100.50
print(price * tax)
# print(price + _) # only works in interactive mode
# print(round(_, 2)) # round to 2 decimal places. only works in interactive mode

# Binary numbers
print(0b10)  # binary

# Octal and Hexadecimal Numbers
print(0o177)  # octal
print(0x9FF)  # hexadecimal

# Exponent
print(3e8)  # 3 * 10^8

# Planck constant
print(6.62607e-34)  # 6.62607 * 10^-34

# Strings
print("spam eggs")  # single quotes
print("doesn't")  # use \' to escape the single quote...
print("doesn't")  # ...or use double quotes instead
print('"Yes," they said.')
print('"Yes," they said.')
print('"Isn\'t," they said.')
print("First line.\nSecond line.")  # \n means newline
print("C:\some\name")  # here \n means newline!
print(r"C:\some\name")  # note the r before the quote
print(
    """\ 
      Usage: thingy [OPTIONS]
              -h                        Display this usage message
              -H hostname               Hostname to connect to
      """
)
print(3 * "un" + "ium")  # 3 times 'un', followed by 'ium'

word = "Python"
print(word[0])  # character in position 0
print(word[5])  # character in position 5
print(word[-1])  # last character
print(word[-2])  # second-last character
print(word[-6])  # first character

print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)
print(word[:2])  # characters from the beginning to position 2 (excluded)
print(word[4:])  # characters from position 4 (included) to the end
print(word[-2:])  # characters from the second-last (included) to the end
print(word[4:42])  # out of range slice indexes are handled gracefully
print(word[42:])  # out of range slice indexes are handled gracefully
print(word[:2] + word[2:])  # slicing out of range is handled gracefully
print(word[:4] + word[4:])  # slicing out of range is handled gracefully
print("J" + word[1:])  # slicing out of range is handled gracefully
print(word[:2] + "py")  # slicing out of range is handled gracefully

s = "supercalifragilisticexpialidocious"
print(len(s))  # length of string

print("temperatures and facts about the moon".title()) # capitalize the first letter of each word

# Split str¡ngs
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures .split()
print(temperatures_list)

# Search in strings
print("Moon" in "This text will describe facts and challenges with space travel") # search for a substring

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))

# String formatting
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))

# f-strings
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")

subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)


# Lists
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])  # indexing returns the item
print(squares[-1])
print(squares[-3:])  # slicing returns a new list
print(squares[:])  # slicing returns a new list
print(squares + [36, 49, 64, 81, 100])  # concatenation returns a new list

cubes = [1, 8, 27, 65, 125]  # something's wrong here
print(4**3)  # the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
print(cubes)
cubes.append(216)  # add the cube of 6
cubes.append(7**3)  # and the cube of 7
print(cubes)

letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters)
letters[2:5] = ["C", "D", "E"]  # replace some values
print(letters)
letters[2:5] = []  # now remove them
print(letters)
letters[:] = []  # clear the list by replacing all the elements with an empty list
print(letters)
letters = ["a", "b", "c", "d"]
print(len(letters))

a = ["a", "b", "c"]
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

# Remove items from a list
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

# Find items in a list
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

# Use min() and max() on lists
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 12650 # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")

# Join lists
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Sort lists
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# First Steps Towards Programming
a, b = 0, 1
while a < 1000:
    print(a, end=",")
    a, b = b, a + b