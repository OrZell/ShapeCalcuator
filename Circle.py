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

    def __len__(self):
        return self.get_perimeter()

    def __lt__(self, other):
        return super().__lt__(other)

    def __le__(self, other):
        return super().__le__(other)

    def __eq__(self, other):
        return super().__eq__(other)

    def __ne__(self, other):
        return super().__ne__(other)

    def __ge__(self, other):
        return super().__ge__(other)

    def __gt__(self, other):
        return super().__gt__(other)