# AI log: для перевірки власного коду, пошуку помилок та отримання пояснень
class Dog:
    age_factor = 7
    def __init__(self, age):
        self.validate(age)
        self.age = age


    def validate(self, age):
        if not isinstance(age, int | float):
            raise TypeError("not number")


    def human_age(self):
        return round(self.age * self.age_factor, 2)

    # просто age_factor без self не працює,
    # тому що атрибути класу не входять автоматично до LEGB-пошуку імен


dog_1 = Dog(3)
print(dog_1.human_age())

dog_2 = Dog(2.5)
print(dog_2.human_age())

try:
    Dog("three")
except TypeError as t:
    print(t)
