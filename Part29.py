# Composition Has-A Relationship


class Engine:

    def __init__(self, cc):
        self.capacity = cc

    def start(self):
        print("Engine Started")

    def stop(self):
        print("Engine Stopped")

# =============================================


class Car:
    def __init__(self, name, cc):
        self.name = name
        self.engine = Engine(cc)    #object creation

    def run(self):
        print(self.engine)
        self.engine.start()
        print("car is running")

# =============================================


c1 = Car("Ferrari", 3700)
c1.run()