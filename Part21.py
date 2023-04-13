# Creating Static Method
# A method that is independent and universally available

class Student:
    uni_name = "BRACU"  # class variable

    def __init__(self, name, Id):  # constructor
        self.name = name  # instance variable
        self.id = Id

    def details(self):  # instance method
        # Student.counter += 1
        print("Name: ", self.name, "ID : ", self.id, Student.uni_name)

    @classmethod  # decorator
    def up_uni_name(cls, u_name):  # class method
        cls.uni_name = u_name

    @staticmethod
    def check_department(Id):
        if Id[3:5] == "01" : print("CSE")
        elif Id[3:5] == "41" : print("CS")


Student.check_department("19141345")

s1 = Student("Bob", 11)

s1.details()

Student.check_department("19101289")