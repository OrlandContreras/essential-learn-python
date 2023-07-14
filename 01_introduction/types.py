# Numbers
print(1 + 1)  # addition
print(50 - 5 * 6)  # multiplication and subtraction
print((50 - 5 * 6) / 4)  # division always returns a floating point number
print(8 / 5)  # division always returns a floating point number
print(17 / 3)  # division always returns a floating point number
print(17 // 3)  # floor division discards the fractional part
print(17 % 3)  # the % operator returns the remainder of the division
print(5 * 3 + 2)  # result * divisor + remainder
print(5**2)  # 5 squared
print(2**7)  # 2 to the power of 7
# print(n) # try to access an undefined variable

tax = 12.5 / 100
price = 100.50
print(price * tax)
# print(price + _) # only works in interactive mode
# print(round(_, 2)) # round to 2 decimal places. only works in interactive mode

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

# First Steps Towards Programming
a, b = 0, 1
while a < 1000:
    print(a, end=",")
    a, b = b, a + b