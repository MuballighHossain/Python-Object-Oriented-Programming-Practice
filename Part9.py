class Student:
    def __init__(self, name, Id):
        self.name = name
        self.id = Id

    def __init__(self, name, Id, cg):
        self.name = name
        self.id = Id
        self.CGPA = cg


s1 = Student("carol", 33)
s2 = Student("Bob", 11, 4.0)