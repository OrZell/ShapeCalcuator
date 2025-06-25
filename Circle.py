import math
import  Shape

class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.Name = 'Circle'
        self.Radius = radius

    def get_area(self):
        return self.Radius*2*math.pi

    def __str__(self):
        return f'Kind: {self.Name}, Radius: {self.Radius}'