# AI log: запитувала про sys.path і пошук модулів
import sys
sys.path.insert(0, "other_folder")
from prices import with_discount

import prices
print(prices.__file__)
print(sys.path)

# ми бачимо першою в списку директорію, з якої запущено файл, тому спочатку Пайтон шукає
# імʼя в папці з відки запущено