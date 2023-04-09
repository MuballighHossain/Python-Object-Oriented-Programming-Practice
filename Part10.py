class Student:
    # def __init__(self, name, Id):
    #     self.name = name
    #     self.id = Id

    # def __init__(self, name, Id, cg):
    #     self.name = name
    #     self.id = Id
    #     self.cg = cg

    def __init__(self, *info):
        if len(info) == 3:
            self.name = info[0]
            self.id = info[1]
            self.cg = info[2]
        elif len(info) == 2:
            self.name = info[0]
            self.id = info[1]
        elif len(info) == 1:
            self.name = info[0]

        print("A student object is created")


s1 = Student("Carol", 33, 3.95)
s2 = Student("bob", 11)
s3 = Student("mub")
s4 = Student()
