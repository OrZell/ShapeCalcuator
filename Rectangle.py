import Shape

class Rectangle(Shape):

    def __init__(self, a, b):
        self.Name = 'Rectangle'
        self.A = a
        self.B = b

    def get_area(self):
        return self.A * self.B

    def get_perimeter(self):
        return (self.A + self.B)*2

    def __str__(self):
        return f'Kind: {self.Name}, A: {self.A}, B: {self.B}'

    def __add__(self, other):
        return self.get_area() + other.get_area()
