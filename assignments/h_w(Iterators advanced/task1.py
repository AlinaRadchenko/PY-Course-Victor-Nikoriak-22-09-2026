# AI log: використовувала для пошуку помилки в умовах завершення ітерації при додатному та від'ємному step
# для пояснення, чому ValueError не виникала під час створення об'єкта без виклику next()
class InRange:
    def __init__(self, start, end, step=1):
        if isinstance(start, int) and isinstance(end, int) and isinstance(step, int):
            self.start = start
            self.end = end
            self.step = step
            self.index_it = self.start
        else:
            raise TypeError("start, end and step must be integers")

    def __iter__(self):
        return self

    def __next__(self):
        if self.step == 0:
            raise ValueError("step cannot be zero")

        if self.step > 0:
            if self.index_it >= self.end:
                raise StopIteration

        elif self.step < 0:
            if self.index_it <= self.end:
                raise StopIteration

        i = self.index_it
        self.index_it += self.step
        return i


try:
    r = InRange(0, 5, 0)
    next(r)
except ValueError as e:
    print(e)

r = InRange(0, 3)
print(list(r))
print(list(r))

print(list(InRange(0, 5)))
print(list(InRange(10, 0, -3)))

# очікую, що перший виклик list(r) поверне [0, 1, 2], він повністю проходить ітератор
# коли ітератор доходить до кінця, викликається StopIteration
# початкове значення автоматично не відновлюється
# тому другий виклик list(r) поверне порожній список []

# Також очікую:
# InRange(0, 5) поверне [0, 1, 2, 3, 4].
# InRange(10, 0, -3) поверне [10, 7, 4, 1].
# InRange(5, 1) поверне [].

assert list(InRange(0, 5)) == list(range(0, 5))
assert list(InRange(10, 0, -3)) == [10, 7, 4, 1]
assert list(InRange(5, 1)) == []

# Старий генератор
# def in_range(start, end, step = None):
#     if step == 0:
#         raise ValueError("step cannot be zero")
#     if step is None:
#         if start > end:
#             step = -1
#         else:
#             step = 1
#
#     if start < end:
#         i = start
#         while i < end:
#             yield i
#             i += step
#     elif start > end:
#         i = start
#         while i > end:
#             yield i
#             i -= abs(step)
#
#
# print(list(in_range(5, 1, 2)))
# print(list(in_range(2, 7)))
# print(list(in_range(10, 0, -3)))
# print(list(in_range(5, 1)))
# print(list(in_range(2, 7, 0)))