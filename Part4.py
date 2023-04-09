class Dog:

    def __init__(self, name, color):
        self.name = name #instance variable
        self.color = color #instance variable

    def update_color(self, color): #instance method, we are parsing a parameter for the designated variable
        self.color = color #updating color variable

    def poke(self): #instance method
        print(self.color, self.name, "is smiling")
#object
d1 = Dog("rover", "brown")
d2 = Dog("tommy", "white")

d1.poke()
d2.poke()

d1.update_color("black") #invoking method to update variables
d1.poke()

d2.update_color("red")
d2.poke()

print(d1.__dict__) #built in method to see attributes in respect to an object shown in a dictionary manner
print(dir(d2))  #built in methods and attributes in respect to an object shown in a list manner