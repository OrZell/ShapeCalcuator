from math import pi
from Shape import Shape

class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.Name = 'Circle'
        self.Radius = radius

    def get_area(self):
        return self.Radius*2*pi

    def get_perimeter(self):
        return pi*pow(self.Radius, 2)

    def __str__(self):
        return f'Kind: {self.Name}, Radius: {self.Radius}'

    def __add__(self, other):
        return self.get_area() + other.get_area()