import Shape

class Rectangle(Shape):

    def __init__(self, a, b):
        super().__init__()
        self.Name = 'Rectangle'
        self.A = a
        self.B = b

    def get_area(self):
        return self.A * self.B

    def __str__(self):
        return f'Kind: {self.Name}, A: {self.A}, B: {self.B}'