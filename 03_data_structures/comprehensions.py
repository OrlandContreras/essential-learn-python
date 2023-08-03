squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

squares = list(
    map(lambda x: x**2, range(10))
)  # Equivalent to squares = [x**2 for x in range(10)]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)
print(list(zip(*matrix)))

a = {x for x in "abracadabra" if x not in "abc"}
print(a)

# Cube - a three-dimensional array (3x3x3)
cube = [
    [[":(", "x", "x"], [":)", "x", "x"], [":(", "x", "x"]],
    [[":)", "x", "x"], [":(", "x", "x"], [":)", "x", "x"]],
    [[":(", "x", "x"], [":)", "x", "x"], [":)", "x", "x"]],
]

print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'
