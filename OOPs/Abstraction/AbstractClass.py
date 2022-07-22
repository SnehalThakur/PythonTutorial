from abc import ABC, abstractmethod  # abc =  Abstract Base Class
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self, radius):
        print("This is Circle class")
        areaOfCircle = pi * radius * radius
        # areaOfCircle = pi * r * r
        print("Area of a Circle is", areaOfCircle)


class Square(Shape):
    def area(self, side):
        print("This is Square class")
        # a * a
        areaOfSquare = side * side
        print("Area of a Square is", areaOfSquare)


class Triangle(Shape):
    def area(self, l, b, h):
        print("This is Triangle class")
        # 1/2 * l * b * h
        areaOfTriangle = (1 / 2 * l * b * h)
        print("Area of a Triangle is", areaOfTriangle)


# Creating an object of Circle class
circle = Circle()
circle.area(5)
print("==================")
# Creating an object of Square class
square = Square()
square.area(10)
print("======================")
# Creating an object of Triangle class
triangle = Triangle()
triangle.area(10, 12, 15)
print("======================")
shape = Shape()
print(shape)