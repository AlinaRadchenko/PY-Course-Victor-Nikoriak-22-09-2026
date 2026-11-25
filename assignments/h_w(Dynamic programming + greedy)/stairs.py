# AI log: виникла помилка у ways_table, я не врахувала початкове значення table[0]
# за допомогою підказок знайшла та виправила помилку

# ways_naive(20) - приблизно 100 000 викликів, рекурсія багаторазово обчислює однакові значення
# ways_memo(20) 20 викликів, бо @functools.cache запам'ятовує результати для вже обчислених аргументів
import functools
def ways_naive(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2) + ways_naive(n - 3)

@functools.cache
def ways_memo(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2

    return ways_memo(n-1) + ways_memo(n-2)+ ways_memo(n-3)

def ways_table(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2

    table = [0] * (n + 1)
    table[0] = 1
    table[1] = 1
    table[2] = 2

    for i in range(3, n + 1):
        table[i] = table[i - 1] + table[i - 2] + table[i - 3]

    return table[n]


print(ways_naive(20))
assert [ways_table(n) for n in range(8)] == [1, 1, 2, 4, 7, 13, 24, 44]
assert ways_table(30) == 53798080
assert all(ways_naive(n) == ways_memo(n) == ways_table(n) for n in range(15))
