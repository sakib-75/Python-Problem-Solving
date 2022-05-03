# Python code to demonstrate how parent constructors are called.
# Calling constructor of parent class

# parent class
class Person:

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def show_person(self):
        print("Name:", self.name)
        print("ID:", self.idnumber)


# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

    def show_employee(self):
        self.show_person()
        print("Salary:", self.salary)
        print("Post:", self.post)


p = Person("sakib", 54)
p.show_person()

# creation of an object variable or an instance
e = Employee('Raju', 50, 15000, "Intern")

# calling a function of the class Person using its instance
e.show_employee()
