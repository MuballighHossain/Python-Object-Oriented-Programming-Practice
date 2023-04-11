# Getter Setter Method


class Student:
    def __init__(self, name, Id):
        self.name = name    # public instance variable
        self.__id = Id      # private instance variable

    def details(self):
        print("Name: ", self.name, "ID: ", self.__id)

    def set_ID(self, Id):
        if Id > 0:
            self.__id = Id  # name mangling
        else:
            print("enter valid ID")

    def get_ID(self):
        return self.__id

    def set_name(self, name):
        self.name = name  # name mangling

    def get_name(self):
        return self.name


s1 = Student("bob", 11)
s2 = Student("carol", 24)

s1.details()
s2.details()

s1.set_ID(55)
print(s1.get_ID())
s2.set_ID(33)
print(s2.get_ID())

s1.set_name("test")
print(s1.get_name())

s1.details()

