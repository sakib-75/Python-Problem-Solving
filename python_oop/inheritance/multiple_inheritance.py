# Python example to show the working of multiple inheritance

class Base1:
    def __init__(self, str1):
        self.str1 = str1
        print("Base 1")


class Base2:
    def __init__(self, str2):
        self.str2 = str2
        print("Base 2")


class Derived(Base1, Base2):
    def __init__(self, a, b):
        # Calling constructors of Base1 and Base2 classes
        Base1.__init__(self, a)
        Base2.__init__(self, b)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)


ob = Derived("Class 1", "Class 2")
ob.printStrs()
