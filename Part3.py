class Car:
    def __init__(self, name, model):
        self.name = name    #instance variable
        self.model_year = model     #instance variable
        self.wheel = 4  #instance variable

    def view(self):     #instance method
        print("The model year of this ", self.name, "is ", self.model_year)
        print("wheels are ", self.wheel)


c1 = Car("BMW", 2016)   # creating object 1
c1.view()

c2 = Car("Audi", 2017)  # creating object 2
c2.view()

c2.wheel = 6

c1.view()
c2.view()
