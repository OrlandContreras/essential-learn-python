# Introduction to Python Dictionaries
tel = {"jack": 4098, "sape": 4139}
tel["guido"] = 4127
print(tel)

del tel["sape"]
tel["irv"] = 4127
print(tel)

print(list(tel))
print(sorted(tel))

print("guido" in tel)
print("jack" not in tel)

print(dict([("sape", 4139), ("guido", 4127), ("jack", 4098)]))

# Create a dictionary
planet = {
    "name": "Earth", 
    "age": 4.5, 
    "diamater": 12742
}

# Read dictionary values
print(planet.get('name'))

# Modify dictionary values
planet.update({'name': 'Makemake'})

