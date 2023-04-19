# Abstract

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        print("Eating")


class Dog(Animal):

    def make_sound(self):
        print("Barking")


class Cat(Animal):

    def make_sound(self):
        print("Meaow")


class Snake(Animal):

    def make_sound(self):
        print("ssss")


d1 = Dog()
d1.make_sound()

c1 = Cat()
c1.make_sound()

s1 = Snake()
s1.make_sound()

d1.eat()
