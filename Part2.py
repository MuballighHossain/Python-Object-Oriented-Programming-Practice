# class
class House:

    def __init__(self):
        # attributes or instance variables
        self.window = 4
        self.door = 2
    # instance method

    def view(self):
        print(self.window, "windows", self.door, "doors")

# object

h1 = House()
h2 = House()

h1.window = 6
h2.door = 3
h1.view()
h2.view()