class Shape:

    def __init__(self):
        pass

    def get_area(self):
        pass

    def __str__(self):
        return 'This Is The Base Class Of Shape'

    def __add__(self, other):
        return self.get_area() + other.get_area()