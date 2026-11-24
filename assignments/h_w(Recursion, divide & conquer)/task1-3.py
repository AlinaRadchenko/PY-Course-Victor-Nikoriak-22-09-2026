import sys

def to_power(x, exp):
    print(exp)
    if exp < 0 or isinstance(exp, bool) or not isinstance(exp, int):
        raise ValueError("Invalid value")
    if exp == 0:
        return 1
    if exp == 1:
        return x
    if exp == 2:
        return x * x
    return x * to_power(x , exp -1 )



def mult(a, n):
    if n < 0 or isinstance(n, bool) or not isinstance(n, int):
        raise ValueError("Invalid value")
    if n == 0:
        return 0
    if n == 1:
        return a
    return a + mult(a, n - 1)

assert to_power(2, 3) == 8
assert to_power(3.5, 2) == 12.25
assert to_power(5, 0) == 1

assert mult(2, 4) == 8
assert mult(2, 0) == 0

try:
    to_power(2, -1)   # ValueError
except ValueError as e:
    print(e)

try:
    mult(2, -4)       # ValueError
except ValueError as e:
    print(e)

try:
    mult(2, 2.5)      # ValueError
except ValueError as e:
    print(e)


# Task 2
def reverse(text):
    if len(text) == 0:
        return ""
    if len(text) == 1:
        return text
    if len(text) == 2:
        return text[1] + text[0]
    return reverse(text[1:]) + text[0]


assert reverse("hello") == "olleh"
assert reverse("o") == "o"
assert reverse("") == ""

def is_palindrome(text, index=0):
    if index >= len(text) // 2:
        return True

    if text[index] != text[len(text) -1 - index]:
        return False

    return is_palindrome(text, index + 1)

assert is_palindrome("mom") == True
assert is_palindrome("sassas") == True
assert is_palindrome("o") == True
assert is_palindrome("") == True
assert is_palindrome("moon") == False

# Task 3
# AI log: просила пояснення з перевіркою того, що символ рядка є цифрою від 0 до 9 у завданні sum_of_digits
def sum_of_digits(digits):
    if not isinstance(digits, str):
        raise TypeError
    if digits == "":
        return 0
    if not ("0" <= digits[0] <= "9"):
        raise ValueError("Only digits from 0 to 9 are allowed")

    return int(digits[0]) + sum_of_digits(digits[1:])


assert sum_of_digits("26") == 8
assert sum_of_digits("") == 0

try:
    sum_of_digits(26)
except TypeError:
    print("TypeError: argument must be a string")

try:
    sum_of_digits("2g6")
except ValueError as e:
    print(e)

# AI-resistant:
# викликається to_power(2, 3)
# exp дорівнює 3, функція викликає to_power(2, 2)
# у to_power(2, 2) спрацьовує базовий випадок exp == 2
# функція повертає результат 2 * 2 = 4
# перший виклик отримує значення 4 і обчислює 2 * 4 = 8

sys.getrecursionlimit()
print(sys.getrecursionlimit())
reverse("a" * 1500)

# return reverse(text[1:]) + text[0]
#            ~~~~~~~^^^^^^^^^^
#   [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded
# для усунення можна використати text[::-1]
# це розвертає рядок без побудови ланцюжка рекурсивних викликів
