# AI log: просила пояснення детальне, навіщо потрібен super().__init__() при наслідуванні класів
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print( "This is a person")

class Student(Person):
    def __init__(self, name):
        super().__init__(name)

    def introduce(self):
        super().introduce()
        print("I am a student")

class Teacher(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def introduce(self):
        super().introduce()
        print("I am a teacher.")



teacher = Teacher("Anna", 30000)

print(isinstance(teacher, Person))# -> True, тому що Teacher наслідує Person
print(isinstance(teacher, Student))# -> False, тому що Teacher і Student різні дочірні класи
print(issubclass(Teacher, Person)) # -> True, тому що Teacher є дочірнім класом Person