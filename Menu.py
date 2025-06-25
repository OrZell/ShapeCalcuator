import Shape
import Rectangle
import Square
import Tringle
import Circle
import Hexagon



class Menu:

    @staticmethod
    def menu():
        choice = 0
        user_input = input("Please choose the shape you want to calculate:\n"
                          "1. Rectangle\n"
                          "2. Square\n"
                          "3. Tringle\n"
                          "4. Circle\n"
                          "5. Hexagon\n"
                          "6. Exit\n")
        if user_input == '1':
            choice = 1
        elif user_input == '2':
            choice = 2
        elif user_input == '3':
            choice = 3
        elif user_input == '4':
            choice = 4
        elif user_input == '5':
            choice = 5
        elif user_input == '6':
            choice = 6

        return choice

    @staticmethod
    def enter_radius():
        radius = input('enter the radius of the circle\n')
        try:
            return int(radius)
        except:
            raise 'Err'

    @staticmethod
    def enter_one_side():
        side = input('enter the len of the side\n')
        try:
            return int(side)
        except:
            raise 'Err'

    @staticmethod
    def enter_two_sides():
        sides = input('enter two sides\n').split()
        if  len(sides) != 2:
            raise 'Err'

        for i in sides:
            try:
                int(i)
            except:
                raise 'Err'
        return sides

    @staticmethod
    def check_shape(num):
        if num == 1:
            sides = Menu.enter_two_sides()
            shape = Rectangle.Rectangle(sides[0], sides[1])
        elif num == 2:
            side = Menu.enter_one_side()
            shape = Square.Square(side)
        elif num == 3:
            sides = Menu.enter_two_sides()
            shape = Tringle.Tringle(sides[0], sides[1])
        elif num == 4:
            radius = Menu.enter_radius()
            shape = Circle.Circle(radius)
        elif num == 5:
            side = Menu.enter_one_side()
            shape = Hexagon.Hexagon(side)

    @staticmethod
    def return_area(shape:Shape):
        return shape.get_area()