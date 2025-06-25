class Manager:

    def __init__(self):


    def Menu(self):
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