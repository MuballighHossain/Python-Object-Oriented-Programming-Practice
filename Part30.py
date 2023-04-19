# Abstract
from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod
    def method1(self):
        pass


class B(A):
    @abstractmethod
    def method2(self):
        print("Method 1")


class C(B):

    def method1(self):
        print("Method 1")

    def method2(self):
        print("Method 2")


c = C()
c.method1()
c.method2()