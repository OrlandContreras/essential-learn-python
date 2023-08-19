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

print(
    "temperatures and facts about the moon".title()
)  # capitalize the first letter of each word

# Split str¡ngs
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)

# Search in strings
print(
    "Moon" in "This text will describe facts and challenges with space travel"
)  # search for a substring

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))

# String formatting
mass_percentage = "1/6"
print(
    "On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage
)
print(
    "On the Moon, you would weigh about {} of your weight on Earth.".format(
        mass_percentage
    )
)
print(
    """You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format(
        "Moon", mass_percentage
    )
)

# f-strings
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")

subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)
