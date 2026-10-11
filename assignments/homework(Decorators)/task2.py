# АI log: розбирали форматування args і kwargs, перетворення чисел на рядки через map(str, args),
# а також роботу розбирали перевірку порожнього kwargs та зайву кому у виведенні
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(map(str, args))
        kwargs_str = ""
        if kwargs:
            kwargs_str = ", ".join(f"{i}='{j}'" for i, j in kwargs.items())
            print(f"{func.__name__} called with {args_str}, {kwargs_str}")
        else:
            print(f"{func.__name__} called with {args_str}")
        result = func(*args, **kwargs)
        return result
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

@logger
def test_some2(a, b, c):
    return a

# Очікую add called with 4, 5
# 9
print(add(4, 5))

print(test_some2(2, b="y", c="e"))
# Очікую повернення функції wrapper без @wraps(func), з ним add, бо ми зберігаємо
# інформацію про початкову функцію
print(add.__name__)

