class Cat:
    def __init__(self, color, action):
        self.color = color
        self.action = action

    def view(self):
        print(self.color, "cat is", self.action)

    def compare(self, ct):  # pass by reference
        if self.action == ct.action:
            print("Both cats are", self.action)
        else:
            print("Actions of the cats are different")

    def test(self, num, clr):
        num = num + 5
        clr1 = clr
        clr1[0] = "Green"
        print("Method inside: ", num)
        print("Method inside: ", clr1)


colors = ["Black", "Red", "Yellow", "Blue"]

c1 = Cat("white", "jumping")
c2 = Cat("Brown", "jumping")

c1.view()
c2.view()

c1.compare(c2)

x = 55
c1.test(x, colors)
print("Method outside", x)
print("Method outside", colors)

