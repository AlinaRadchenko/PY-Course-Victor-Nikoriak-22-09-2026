# AL log: отримувала підказки щодо high, low та підрахунку викликів функції
calls = 0
def binary_search(items, target, low=0, high=None):
    global calls
    calls += 1

    if high is None:
        high = len(items) - 1
    if low > high:
        return -1

    mid = (low + high)// 2
    if items[mid] == target:
        return mid
    if items[mid] < target:
        return binary_search(items, target, mid + 1, high)
    else:
        return binary_search(items, target, low, mid - 1)




data = list(range(0, 2000, 2))

assert binary_search(data, 42) == 21
assert binary_search(data, 41) == -1
assert binary_search(data, 1998) == 999
assert binary_search([], 5) == -1

# 1000 елементів, приблизно 10 поділів навпіл
# 1 000 000 елементів, приблизно 20 поділів навпіл
# на кожному рекурсивному виклику ми відкидаємо половину елементів

max_calls = 0
for target in range(-1, 2001):
    calls = 0
    binary_search(data, target)

    if calls > max_calls:
        max_calls = calls

print("Максимальна кількість викликів для 1000 елементів:", max_calls)

big_data = list(range(1_000_000))

calls = 0
binary_search(big_data, 1_000_000)

print("Кількість викликів для 1 000 000 елементів:", calls)