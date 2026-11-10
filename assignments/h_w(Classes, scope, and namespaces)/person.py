# AI log: none
class Person:
    population = 0
    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        Person.population += 1

    def get_greeting(self):
        return f"Hello, my name is {self.first_name} {self.last_name} and I'm {self.age} years old"


    def talk(self):
        print(self.get_greeting())

person_1 = Person("Alina", "Radchenko", 25)
person_2 = Person("Lin", "Kober", 25)
person_1.talk()
person_2.talk()
# Person.population виведе 2, тому що створено два екземпляри класу Person
# population не з'явиться в person_1.__dict__, тому що це атрибут класу, а не екземпляра
print(Person.population)
print(person_1.__dict__)