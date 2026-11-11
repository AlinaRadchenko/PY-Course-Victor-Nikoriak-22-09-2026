# AI log: використовувала для пояснення помилок
class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} say - Some animal sound")

class Dog(Animal):
    def talk(self):
        print(f"{self.name} says - Woof woof woof")


class Cat(Animal):
    def talk(self):
        print(f"{self.name} says - Meow")

def make_sound(animal):
    animal.talk()

class Duck:
    def talk(self):
        print("Quack")


dog = Dog("Rex")
cat = Cat("Liki")

duck = Duck()
# make_sound() працюватиме з Duck,
# тому що клас Duck має свій метод talk()
make_sound(duck)

make_sound(dog)
make_sound(cat)

