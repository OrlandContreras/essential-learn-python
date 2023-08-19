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
planets = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
]

planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

# Find items in a list
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

# Use min() and max() on lists
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 12650  # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print(
    "The lightest a bus would be in the solar system is",
    bus_weight * min(gravity_on_planets),
    "kg",
)
print(
    "The heaviest a bus would be in the solar system is",
    bus_weight * max(gravity_on_planets),
    "kg",
)

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
