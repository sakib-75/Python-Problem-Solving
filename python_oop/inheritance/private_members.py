# Python program to demonstrate private members
# of the parent class

class Class1(object):
    def __init__(self):
        self.c = 21

        # d is private instance variable
        self.__d = 42


class Class2(Class1):
    def __init__(self):
        self.e = 84
        Class1.__init__(self)


obj = Class2()

# produces an error as d is private instance variable
print(obj.d)
