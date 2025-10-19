# OOPAssignment.py
# Chloe Bell
# Code Cumbria - Python OOP Assignment

import math

# Base class
class Shape:
    """Base class for geometric shapes."""
    def area(self):
        pass

    def perimeter(self):
        pass


# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# Rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Isosceles Triangle class
class IsoscelesTriangle(Shape):
    def __init__(self, base, side):
        self.base = base
        self.side = side

    def perimeter(self):
        return (2 * self.side) + self.base

    def area(self):
        height = math.sqrt((self.side ** 2) - ((self.base ** 2) / 4))
        return 0.5 * self.base * height

# Test code
def main():
    print("OOP Assignment - Shape Calculations\n")

    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = IsoscelesTriangle(6, 5)

    print("Circle:")
    print(" Radius:", circle.radius)
    print(" Area:", round(circle.area(), 2))
    print(" Perimeter:", round(circle.perimeter(), 2))
    print()

    print("Rectangle:")
    print(" Length:", rectangle.length, "| Width:", rectangle.width)
    print(" Area:", rectangle.area())
    print(" Perimeter:", rectangle.perimeter())
    print()

    print("Isosceles Triangle:")
    print(" Base:", triangle.base, "| Side:", triangle.side)
    print(" Area:", round(triangle.area(), 2))
    print(" Perimeter:", triangle.perimeter())


if __name__ == "__main__":
    main()