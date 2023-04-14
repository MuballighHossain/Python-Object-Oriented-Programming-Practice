# Inheritance IS-A Relationship

# single inheritance


class Animal:   # parent/ baseClass / superclass

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")

# =============================================


class Dog(Animal):  # childClass / SubClass / derived

    def bark(self):
        print(self.name, "is barking")

# =============================================


a1 = Animal("Jack")
d1 = Dog("Rover")
d1.bark()
d1.eat()
a1.eat()

# a1.bark() -> will not work

# isinstance (object, className)

print(isinstance(a1, Dog))
print(isinstance(a1, Animal))

# issubclass(class, classname)

print(issubclass(Animal, Dog))
print(issubclass(Dog, Animal))