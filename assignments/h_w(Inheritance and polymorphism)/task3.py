# AI log:запитувала про використання self та чому його не потрібно
# використовувати для кожної локальної змінної всередині методів класу
class SquareNumbers:
    def square_nums(self, numbers):
        new_list = []
        for n in numbers:
            result = n ** 2
            new_list.append(result)
        return new_list


class RemovePositives:
    def remove_positives(self, numbers):
        new_list = []
        for n in numbers:
            if n <= 0:
                new_list.append(n)
        return new_list

class FilterLeapYears:
    def filter_leaps(self, numbers):
        new_list = []
        for n in numbers:
            if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
                new_list.append(n)
        return new_list

class Mathematician(SquareNumbers, RemovePositives, FilterLeapYears):
    pass

# спочатку клас перевірить сам себе, потім перший батьківський SquareNumbers ->
# другий RemovePositives -> третій FilterLeapYears -> базовий клас Python
print(Mathematician.__mro__)
m = Mathematician()

# якщо змінити порядок батьківських класів порядок MRO також зміниться
# та всі три методи залишилися доступними через Mathematicia

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

