import Rectangle

class Tringle(Rectangle):

    def __init__(self ,a, b):
        super().__init__(a, b)
        self.Name = 'Tringle'

    def get_area(self):
        return super().get_area()/2

    def __str__(self):
        return super().__str__()