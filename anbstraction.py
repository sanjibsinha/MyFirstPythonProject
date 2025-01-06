from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14 * self.__radius * self.__radius

    def perimeter(self):
        return 2 * 3.14 * self.__radius
    
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def area(self):
        return self.__length * self.__breadth

    def perimeter(self):
        return 2 * (self.__length + self.__breadth)
    
c = Circle(7)
print(c.area())
print(c.perimeter())

r = Rectangle(5, 10)
print(r.area())
print(r.perimeter())

# abs = Shape() # This will raise an error

# Output:
# 153.86
# 43.96
# 50
# 30
# The Shape class is an abstract class that has two abstract methods: area() and perimeter(). The Circle and Rectangle classes inherit from the Shape class and implement the area() and perimeter() methods. The Circle class calculates the area and perimeter of a circle, while the Rectangle class calculates the area and perimeter of a rectangle. The main program creates instances of the Circle and Rectangle classes and calls their area() and perimeter() methods to calculate the area and perimeter of the shapes. The output shows the area and perimeter of the circle and rectangle.
# end of the program