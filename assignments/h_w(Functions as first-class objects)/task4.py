# AI log: none
from functools import reduce

prices = ["120", "80", "45", "300"]

# Bug: map() повертає ітератор, який вичерпується після перебору
# тому перетворюємо його на список, щоб використовувати numbers декілька разів
numbers = list(map(int, prices))
cheap = list(filter(lambda p: p < 100, numbers))
print("Cheap:", cheap)

total = reduce(lambda acc, p: acc + p, numbers)
print("Total:", total)
# Bug: len() викликає функцію одразу
# sorted() потрібна сама функція len, щоб вже потім застосовувати її до кожного елемента
names = sorted(["Olena", "Ira", "Bohdan"], key=len)
print(names)