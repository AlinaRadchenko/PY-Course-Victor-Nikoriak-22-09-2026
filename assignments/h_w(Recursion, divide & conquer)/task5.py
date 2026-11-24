# AI log: допомога з відстеженням глибини рекурсії та виправлення помилки
# також допомога, щодо розуміння логіки коду

import random
import sys
deepest_level = 0

def merge_sort(items, low=0, high=None, level=1):
    global deepest_level

    deepest_level = max(deepest_level, level)

    if high is None:
        high = len(items)

    if (high - low) <= 1:
        return None

    mid = (low + high) // 2

    merge_sort(items, low, mid, level + 1)
    merge_sort(items, mid, high, level + 1)

    i = low
    j = mid
    temp = []

    while i < mid and j < high:
        if items[i] >= items[j]:
            temp.append(items[j])
            j += 1
        else:
            temp.append(items[i])
            i += 1

    while i < mid:
        temp.append(items[i])
        i += 1

    while j < high:
        temp.append(items[j])
        j += 1

    for k in range(len(temp)):
        items[low + k] = temp[k]


# випадковий список із 1000 чисел - 11 рівнів
# відсортований список із 1000 чисел - 11 рівнів
random_data = [random.randint(1, 10000) for _ in range(1000)]

deepest_level = 0
merge_sort(random_data)

print("Випадковий список:", deepest_level)

# відсортований список
sorted_data = list(range(1000))

deepest_level = 0
merge_sort(sorted_data)

print("Відсортований список:", deepest_level)

print("Ліміт рекурсії:", sys.getrecursionlimit())