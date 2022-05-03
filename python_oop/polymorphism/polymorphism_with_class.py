# Polymorphism with class methods

class Bangladesh:
    def capital(self):
        print("Dhaka is the capital of India.")

    def language(self):
        print("Bangla is the most widely spoken language of Bangladesh.")

    def type(self):
        print("Bangladesh is a developing country.")


class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


def country(obj):
    obj.capital()
    obj.language()
    obj.type()


obj_ban = Bangladesh()
obj_usa = USA()

country(obj_ban)
country(obj_usa)

# for country in (obj_ind, obj_usa):
#   country.capital()
#   country.language()
#   country.type()
