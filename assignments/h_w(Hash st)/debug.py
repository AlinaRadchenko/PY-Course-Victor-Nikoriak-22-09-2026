# AI log: просила прояснити детально, як працює two_sum_broken і чому вона повертає однакові індекси
# def is_anagram_broken(a, b):
#     return set(a) == set(b)
# bug: сет не враховує скільки разів літера зустрічається
import time
def is_anagram(a, b):
    a = a.lower().replace(" ", "")
    b = b.lower().replace(" ", "")
    return sorted(a) ==  sorted(b)

# Counter швидший, тому що, проходить по символах один раз
# і рахує їх кількість за O(n)
# sorted() сортує символи зі складністю O(n log n)
print(is_anagram("Listen", "silent"))
print(is_anagram("conversation", "voices rant on"))

def two_sum_broken(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        seen[x] = i
    for i, x in enumerate(nums):
        if target - x in seen:
            return (i, seen[target - x])
    return None
# перший цикл записував усі числа у словник до перевірки
# через це поточне число могло знайти саме себе
# і функція повертала однакові індекси

def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return (seen[target - x], i)
        seen[x] = i

    return None

print(two_sum_broken([3, 1, 4], 6))
print(two_sum([3, 1, 4], 6))
print(two_sum([3, 1, 4], 5))

big = list(range(20_000))

def two_sum_nested(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
    return None

start = time.perf_counter()
print(two_sum(big, -1))
end = time.perf_counter()
elapsed = end - start
print(elapsed)

start = time.perf_counter()
print(two_sum_nested(big, -1))
end = time.perf_counter()
elapsed = end - start
print(elapsed)

# two_sum(big, -1): 0.0010458750002726447 секунд
# two_sum_nested(big, -1): 4.062015083998631 секунд
