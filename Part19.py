# Instance Method , Class Method, Static Method
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


s1 = Student("Bob", 11)
s2 = Student("Tex", 12)
s3 = Student("Carol", 13)
s1.details()
s2.details()
Student.up_uni_name("Brac University")
s1.details()
s2.details()
s1.up_uni_name("test")
s2.details()
