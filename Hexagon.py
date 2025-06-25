from Shape import  Shape

class Hexagon(Shape):

    def __init__(self, a):
        super().__init__()
        self.Name = 'Hexagon'
        self.A = a

    def get_area(self):
        return pow(self.A, 2)*(3 * (pow(3, 0.5)) / 2)

    def get_perimeter(self):
        return self.A * 6

    def __str__(self):
        return f'Kind: {self.Name}, A: {self.A}'

    def __add__(self, other):
        return self.get_area() + other.get_area()