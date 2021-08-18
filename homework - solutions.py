# Write a Python class to reverse a string word by word.

class ReverseText:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(ReverseText().reverse_words('This is text read forwards'))


# Write a Python class which has two methods get_String and print_String.
# get_String accept a string from the user and print_String print the string in upper case.

class IOString:
    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input("Please enter a string: ")

    def print_string(self):
        print(self.str1.upper())


str1 = IOString()
str1.get_string()
str1.print_string()


# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.

class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length * self.width


newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())


# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14


new_circle = Circle(8)
print(new_circle.area())
print(new_circle.perimeter())

# Write a Python program to get the class name of an instance in Python.
import itertools
x = itertools.cycle('ABCD')
print(type(x).__name__)
