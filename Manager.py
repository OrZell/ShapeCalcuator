import Menu

class Manager:

    @staticmethod
    def MainMenu():
        sign = True
        while sign:
            choice = Menu.Menu.menu()
            if choice == 0:
                print('Not valid Input, Try Again.')
                continue
            elif choice == 6:
                print('Bye Bye')
                sign = False
                continue
            shape = Menu.Menu.check_shape(choice)
            print(Menu.Menu.return_area(shape))
