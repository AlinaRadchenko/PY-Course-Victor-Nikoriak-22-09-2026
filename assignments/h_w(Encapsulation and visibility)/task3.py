# AI log: перевірка помилок та пояснення, як виправляти
import math
class Dog:
    age_factor = 7
    def __init__(self, age):
        self.age = age

    def validate(self, age):
        if not (not isinstance(age, bool) and isinstance(age, (int, float))):
            raise TypeError("Age must be an integer or float")
        elif age < 0 or not math.isfinite(age):
            raise ValueError("Age must be non-negative and finite")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self.validate(value)
        self._age = value

    @property
    def human_age(self):
        return round(self._age * self.age_factor, 2)


d = Dog(3)
print(d.human_age)   # 21
d.age = 2.5
print(d.human_age)   # 17.5
Dog("three")        # TypeError
d.human_age = 5      # AttributeError

# в порівнянні з уроку 19:
# перетворили age з публічного атрибута на property
# зберігає звичний синтаксис доступу: dog.age та dog.age = value.
# перетворили human_age з методу на property
# замість dog.human_age() тепер потрібно писати dog.human_age

