import  Rectangle

class Square(Rectangle):

    def __init__(self, a):
        super().__init__(a, a)
        self.Name = 'Square'

    def get_area(self):
        return super().get_area()

    def get_perimeter(self):
        return super().get_perimeter()

    def __str__(self):
        return f'Kind: {self.Name}, A: {self.A}'

    def __add__(self, other):
        return self.get_area() + other.get_area()