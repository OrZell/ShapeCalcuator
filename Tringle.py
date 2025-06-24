import Shape

class Tringle(Shape):

    def __init__(self ,a, b):
        self.Name = 'Tringle'
        self.A = a
        self.B = b

    def get_area(self):
        return (self.A * self.B)/2

    def __str__(self):
        return f'Kind: {self.Name}, A: {self.A}, B: {self.B}'