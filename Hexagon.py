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