# How to make a function

def name_of_the_function():
    # Here is what will be executed
    pass


def say_hi():
    print("Hi")


say_hi()


# passing values into a function
def display(value):
    print("You typed into the function the number: %d" % value)


display(103)


# number = int(input("Please enter a number: "))
# display(number)


def sum(a, b):
    print(a + b)


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
sum(x, y)


def identify(name, date_of_birth, village):
    print("Your name is: %s" % name)
    print("Your age is: %d" % (2021 - date_of_birth))
    print("You come from: %s" % village)


a = input("Name: ")
b = int(input("Year of birth"))
c = input("Village: ")
identify(a, b, c)


def multiply_numbers(i, j):
    return i * j


print(multiply_numbers(6, 9))
