'''
Your program must:

ask the user to enter a word;
use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about string methods and the upper() method very soon – don't worry;
use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
print the uneaten letters to the screen, each one of them on a separate line.

Example input:
Gregory

Expected output:
G
R
G
R
Y
'''

user_word = input("Enter a word: ")

for letter in user_word:
    if letter.upper() == "A":
        continue
    elif letter.upper() == "E":
        continue
    elif letter.upper() == "I":
        continue
    elif letter.upper() == "O":
        continue
    elif letter.upper() == "U":
        continue
    else:
        print(letter.upper())