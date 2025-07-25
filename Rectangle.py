from Shape import Shape

class Rectangle(Shape):
    """Shape type Rectangle"""
    def __init__(self, a, b):
        """Gets two parameters of length and width"""
        super().__init__()
        self.Name = 'Rectangle'
        self.A = a
        self.B = b

    def get_area(self):
        """Calculate ethe area"""
        return self.A * self.B

    def get_perimeter(self):
        """Calculate ethe perimeter"""
        return (self.A + self.B)*2

    def __str__(self):
        return f'Kind: {self.Name}, A: {self.A}, B: {self.B}'

    def __add__(self, other):
        return self.get_area() + other.get_area()

    def __len__(self):
        return self.get_perimeter()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()