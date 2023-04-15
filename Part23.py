# Inheritance / Hierarchical inheritance
class Student:  # parent / super / base class
    def __init__(self, name, Id):
        self.name = name
        self.id = Id

    def details(self):
        print("Name : ", self.name, "ID : ", self.id)

# =======================================================


class CSEStudent(Student):  # child class
    def __init__(self, name, Id, labs):
        super().__init__(name, Id)
        self.no_of_labs = labs

    def cry(self):
        print("CSE student is crying because of ", self.no_of_labs, " labs")

# =======================================================


class BBAStudent(Student):

    def party(self):
        print("Add day party")

# =======================================================


s1 = CSEStudent("Bob", 11, 3)
s2 = BBAStudent("Bob", 36)

s1.details()
s2.details()
s1.cry()
s2.party()

print(help(s1))
