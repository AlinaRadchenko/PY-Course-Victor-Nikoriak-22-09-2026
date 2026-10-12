# AI log: попросила переписати count_chars() з functools.reduce()
import mymod
from functools import reduce

lines = [
    "I am learning Python.",
    "Modules are useful!",
    "This is my test."
]
mymod.test(lines)

# папка з mymod.py має бути в sys.path, щоб Python міг простіше знайти модуль
# ящко файл лежить у папці запуску Python зазвичай знаходить його автоматично
# якщо він в іншій папці, можна додати шлях до sys.path, як я робила в prices.py

# Варіант від AI
#def count_chars(lines):
    #return reduce(lambda total, line: total + len(line), lines, 0)

# Перевірка документації Python:
# AI використовує модуль functools, він існує у стандартній бібліотеці
# functools.reduce - існує, len() - вбудована функція, lambda - синтаксис Python