import  Shape

class Hexagon(Shape):

    def __init__(self, a):
        self.Name = 'Hexagon'
        self.A = a

    def get_area(self):
        return pow(self.A, 2)*(3 * (pow(3, 0.5)) / 2)

    def __str__(self):
        return f'Kind: {self.Name}, A: {self.A}'