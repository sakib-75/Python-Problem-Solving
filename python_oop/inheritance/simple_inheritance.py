# A Python program to demonstrate inheritance

class Person:

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True


per = Person("Person 1")  # An Object of Person
print(per.getName(), "Employee:", per.isEmployee())

emp = Employee("Person 2")  # An Object of Employee
print(emp.getName(), "Employee:", emp.isEmployee())
