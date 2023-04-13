# Creating Factory Method
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

    @classmethod
    def from_string(cls, info):
        name, Id = info.split('-')
        obj = cls(name, Id)     # calling default constructor 
        return obj


s1 = Student("Bob", 11)
s2 = Student.from_string("Tex-47")

s1.details()
s2.details()
