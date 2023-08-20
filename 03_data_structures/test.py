# Item 1
my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

# Item 2
var = 1
while var < 10:
    print("#")
    var = var << 1
    # print(var)

# Item 3:
nums = [1, 2, 3]
vals = nums
del vals[1:2]
print(nums)
print(vals)

# Item 4:
z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)

# Item 5:
a = 1
b = 0
c = a & b
print(c)
d = a | b
print(d)
e = a ^ b
print(e)

print(c + d + e)

# Item 6:
vals = [0, 1, 2]
vals.insert(0, 1)
print(vals)
del vals[1]
print(vals)

# Item 7:
i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print("*")
