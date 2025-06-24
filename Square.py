import  Shape

class Square(Shape):

    def __init__(self, a):
        self.Name = 'Square'
        self.A = a

    def get_area(self):
        return pow(self.A, 2)

    def __str__(self):
        return f'Kind: {self.Name}, A: {self.A}'