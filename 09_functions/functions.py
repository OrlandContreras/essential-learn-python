def hello(name):  # Defining a function
    print("Hello " + name)  # Function body


name = input("Enter your name: ")

hello(name)  # Calling a function


# Positional arguments
def introduction(first_name: str, last_name: str):
    print(f"Hello, my name is {first_name} {last_name}")


introduction("John", "Doe")
introduction("Luke", "Skywalker")
introduction("Clark", "kent")
introduction("Bruce", "Wayne")

# Keyword arguments
introduction(first_name="John", last_name="Doe")
introduction(last_name="Skywalker", first_name="Luke")
introduction(first_name="Clark", last_name="kent")


# Default arguments
def introduction_v2(first_name: str, last_name: str = "Doe"):
    print(f"Hello, my name is {first_name} {last_name}")


introduction_v2("John")
introduction_v2("Luke", "Skywalker")
introduction_v2()


# Summary functions
def address(street, city, postal_code):
    print(f"Your address is: {street}, {city}, {postal_code}")


street = input("Enter your street: ")
city = input("Enter your city: ")
postal_code = input("Enter your postal code: ")

address(street, city, postal_code)
