# Class or Static Variable
class Student:
    counter = 0 # class or static variable

    def __init__(self, name, Id):  #constructor
        self.name = name  # instance variable
        self.id = Id
        Student.counter += 1

    def details(self):     #instance method
        # Student.counter += 1
        print("Name: ", self.name, "ID : ", self.id, "Student Count", Student.counter)


print("Student Counter", Student.counter)
s1 = Student("Bob", 11)
s2 = Student("Tex", 12)
s3 = Student("Carol", 13)
print("Student Counter", Student.counter)
s1.details()
s2.details()
s3.details()
print("Student Counter", Student.counter)
s1.details()
s1.details()

