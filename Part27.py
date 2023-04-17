# Method Overriding


class A:
    def __init__(self):
        print("__init__ of class A")

    def method1(self):
        print("Always study")

    def method2(self):
        print("Test")

# =======================================================


class B(A):
    def __init__(self):
        pass

    def method1(self):
        super().method1()
        print("Always party")

# =======================================================


b1 = B()
b1.method1()
b1.method2()