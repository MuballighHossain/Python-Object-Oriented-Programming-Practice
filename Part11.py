class Student:

    def __init__(self, **info):
        if len(info) == 3:
            self.name = info['name']
            self.id = info['Id']
            self.cg = info['CG']
        elif len(info) == 2:
            self.name = info['name']
            self.id = info['Id']
        elif len(info) == 1:
            self.name = info['name']

        print("A student object is created")


s1 = Student(name="Carol", Id=33, CG=3.95)
s2 = Student(name="bob", Id=11)
s3 = Student(name="mub")
s4 = Student()