# __str__()


class Student:

    def __init__(self, name, Id):
        self.name = name
        self.id = Id
        print(self)

    def __str__(self):
       return "This is " +  self.name


s1 = Student("Bob", 11)
s2 = Student("Carol", 33)

print(s1)
print(s2.__str__())


