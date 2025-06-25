from Rectangle import Rectangle

class Square(Rectangle):
    """Shape type Square"""
    def __init__(self, a):
        super().__init__(a, a)
        self.Name = 'Square'

    def get_area(self):
        """Calculate ethe area"""
        return super().get_area()

    def get_perimeter(self):
        """Calculate ethe Perimeter"""
        return super().get_perimeter()

    def __str__(self):
        return f'Kind: {self.Name}, A: {self.A}'

    def __add__(self, other):
        return self.get_area() + other.get_area()

    def __len__(self):
        return super().__len__()

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