# Multilevel Inheritance
class Student:  # Grand Parent
    def __init__(self, name, Id):
        self.name = name
        self.id = Id

    def details(self):
        print("Name : ", self.name, "ID : ", self.id)


# =======================================================


class CSEStudent(Student):  # Parent
    def __init__(self, name, Id, labs):
        super().__init__(name, Id)
        self.no_of_labs = labs

    def cry(self):
        print("CSE student is crying because of ", self.no_of_labs, " labs")


# =======================================================


class CSEFresher(CSEStudent):  # Child

    def enroll_CSE110(self):
        print(self.name, "Enrolled in CSE-110")


# =======================================================

s1 = CSEStudent("bob", 11, 3)
s2 = CSEFresher("Carol", 55, 1)
s2.details()
s1.details()
s1.cry()
s2.cry()
s2.enroll_CSE110()
# s1.enroll_CSE110() -> This will not work
