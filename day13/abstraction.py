# abstraction(추상화)

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius


    def area(self):
        return 3.14 * self.radius ** 2

# rectangle, triangle

class Rectangle(Shape):
    def




class T





