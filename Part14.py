# Encapsulation: Public Private Variable

class Student:
    def __init__(self, name, Id):
        self.name = name    # public instance variable
        self.__id = Id      # private instance variable

    def details(self):
        print("Name: ", self.name, "ID: ", self.__id)

    def update_ID(self, Id):
        if (Id > 0):
            self.__id = Id  # name mangling
        else:
            print("enter valid ID")


s1 = Student("bob", 11)
s2 = Student("carol", 24)

s1.details()
s2.details()

s1.update_ID(-666)
s1.update_ID(666)
s1.details()
# s1.__id = -66
# print(s1.__dict__)

# print(s1.__id)
