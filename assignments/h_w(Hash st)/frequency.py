# AI log: None
from collections import Counter
text = "the cat and the dog and the bird and the cat".split()
counts = {}

for word in text:
    counts[word]= counts.get(word, 0) + 1
print(counts)

print(sorted(counts.items(), key = lambda kv: kv[1], reverse=True)[:3])


counts_2 = Counter(text)
print(counts_2.most_common(3))


def two_sum(nums, target):
    seen = {}
    for i, j in enumerate(nums):
        if target - j in seen:
            return (seen[target - j], i)
        seen[j] = i
    return None

nums = [11, 2, 15, 7, 26, 19]
# return (1, 3)
print(two_sum(nums, 9))
# return (0, 2)
print(two_sum(nums, 26))
# return None
print(two_sum(nums, 100))
# функція повертає (1, 3), індекс першого зустрінутого числа
# а потім другого