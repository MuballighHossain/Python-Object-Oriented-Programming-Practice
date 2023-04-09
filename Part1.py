#class
class Student:
    def __init__(self, name, Id):
        # instance variables
        self.name = name
        self.id = Id

    # method
    def details(self):
        print("Name: ", self.name, "ID: ", self.id)


# object
# variable = class_name()
s1 = Student("Bob", 11)
s2 = Student("Carol", 22)

s1.details()    # method must be in reference to object

s1.id = 33

s1.details()
s2.details()