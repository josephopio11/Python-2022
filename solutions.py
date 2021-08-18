class Rectangle:
    def __init__(self, a, b):
        self.length = a
        self.width = b

    def rectangle_area(self):
        return self.length * self.width

    def rectangle_perimeter(self):
        return (self.length + self.width) * 2


rectangle1 = Rectangle(9, 6)

print(rectangle1.rectangle_area())
print(rectangle1.rectangle_perimeter())
