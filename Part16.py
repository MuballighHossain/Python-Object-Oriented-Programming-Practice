# Private Method


# class ABC:
#     def __init__(self, x, y):
#         self.x = x
#         self.__y = y
#
#     def details(self):
#         print(self.x, self.__y)
#
# a1 = ABC(5,6)
# a2 = ABC(15,17)
#
# print(a1.x)
# print(a1.y)  # will show error
# a1.details()


class Student:
    def __init__(self, name, Id):
        self.name = name  # public instance variable
        self.__id = Id  # private instance variable

    def details(self):
        print("Name: ", self.name, "ID: ", self.__id)
        self.__method()

    def __method(self):
        print("private method is executed")


s1 = Student("bob", 11)
s2 = Student("carol", 24)

# s1.__method()  # will throw error

s1.details()
