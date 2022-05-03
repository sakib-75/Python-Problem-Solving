# Polymorphism with Inheritance

class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class Sparrow(Bird):
    def intro(self):
        Bird.intro(self)
        print("This is sparrow")

    def flight(self):
        print("Sparrows can fly.")


class Ostrich(Bird):
    def intro(self):
        Bird.intro(self)
        print("This is ostrich")

    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = Sparrow()
obj_ost = Ostrich()

for bird in (obj_bird, obj_spr, obj_ost):
    bird.intro()
    bird.flight()
