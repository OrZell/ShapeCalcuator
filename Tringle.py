from Rectangle import Rectangle

class Tringle(Rectangle):

    def __init__(self ,a, b):
        super().__init__(a, b)
        self.Name = 'Tringle'

    def get_area(self):
        return super().get_area()/2

    def get_perimeter(self):
        return super().get_perimeter()/2

    def __str__(self):
        return super().__str__()

    def __add__(self, other):
        return super().__add__(other)/2

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