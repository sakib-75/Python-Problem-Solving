# Class or Static Variables in Python

class CSStudent:
    stream = 'cse'  # Class/Static Variable

    def __init__(self, name, roll):
        self.name = name  # Instance/Non-Static Variable
        self.roll = roll  # Instance/Non-Static Variable


# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print(a.stream)  # prints "cse"
print(a.name)  # prints "Geek"
print(a.roll)  # prints "1"
print(b.stream)  # prints "cse"
print(b.name)  # prints "Nerd"
print(b.roll)  # prints "2"

# Class variables can be accessed using class name also
print(CSStudent.stream)  # prints "cse"

# Now if we change the stream for just a, it won't be changed for b
a.stream = 'ece'
print(a.stream)  # prints 'ece'
print(b.stream)  # prints 'cse'

# To change the stream for all instances of the class we can change it directly from the class
CSStudent.stream = 'mech'

print(a.stream)  # prints 'ece'
print(b.stream)  # prints 'mech'
