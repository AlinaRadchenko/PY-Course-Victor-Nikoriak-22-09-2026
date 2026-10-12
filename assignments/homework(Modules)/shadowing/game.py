# AI Log: намагалася виправити проблему імпорту власного
# random.py замість стандартного модуля Python, змінювали sys.path
# та перевіряли шляхи до файлів, але вирішити проблему не вдалося

import sys
sys.path.insert(0, "/Users/alina/PycharmProjects/PY-Course-Victor-Nikoriak-22-09-2026/assignments/homework(Modules)/shadowing")

import random

print(random.__file__)
print(random.randint(1, 6))

# Очікую: Python імпортує мій random.py та виводить "this is my random", а потім виникає AttributeError,
# тому, що в моєму модулі немає атрибута randint
# у моєму випадку Python продовжує використовувати стандартний модуль random,
# і мені не вдалося налаштувати імпорт локального модуля