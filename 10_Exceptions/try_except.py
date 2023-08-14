# "It’s better to beg for forgiveness than to ask for permission"
# Try and Except Block
try:
    value = int(input("Enter a number: "))
    print("The reciprocal of ", value, " is", 1 / value)
except:
    print("I do not know what to do. ")

# Try and Except Block with specific exception
try:
    value = int(input("Enter a natural number: "))
    print("The reciprocal of ", value, " is", 1 / value)
except ValueError:
    print("I do not know wehat to do. ")
except ZeroDivisionError:
    print("Division by zero is no allowed in our Universe.")
except:  # Exceptio by default
    print("Something strange has happened here... Sorry!")

"""
Some useful exceptions:
- ZeroDivisionError
- ValueError
- TypeError
- AttributeError
- SyntaxError

As an old developer's saying states: "it's a feature, not a bug" 
(please don't use this phrase to justify your code's weird behavior).

Some useful tips:
---------------------
1. Try to tell someone (for example, your friend or coworker) what your code is expected to do and how it actually behaves.
Be concrete and don't omit details. Answer all questions your helper asks. 
You'll likely realize the cause of the problem while telling your story, as speaking activates these parts of your brain which remain idle during coding. 
If no human can help you with the problem, use a yellow rubber duck instead. 
We're not kidding.

2. Try to isolate the problem. You can extract the part of your code that is suspected of being responsible for your troubles and run it separately. 
You can comment out parts of the code that obscure the problem. Assign concrete values to variables instead of reading them from the input. 
Test your functions by applying predictable argument values. Analyze the code carefully. Read it aloud.

3. If the bug has appeared recently and didn't show up earlier, analyze all the changes you've introduced into your code 
– one of them may be the reason.

4. Take a break, drink a cup of coffee, take your dog and go for a walk, read a good book for a moment or two, make a phone call to your best friend 
– you'll be surprised how often it helps.

5. Be optimistic – you'll find the bug eventually; we promise you this.
"""
