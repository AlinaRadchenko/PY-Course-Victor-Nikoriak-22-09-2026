# AI log: розбирали як, попрацювати з файлом, що відкиваємо
# розділити текст на слова, очистити їх від пунктуації
import string


def group_anagrams(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)

    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

words = text.split()

clean_words = []

for word in words:
    word = word.lower()
    word = word.strip(string.punctuation)

    if word:
        clean_words.append(word)

clean_words = list(set(clean_words))
groups = group_anagrams(clean_words)
groups = [group for group in groups if len(group) > 1]
biggest_groups = sorted(groups, key=len, reverse=True)[:3]

print(biggest_groups)

# AI version:
# def group_anagrams(words):
#     anagrams = {}
#     for word in words:
#         key = "".join(sorted(word.lower()))
#         anagrams.setdefault(key, []).append(word)
#     return list(anagrams.values())

# Порівняння:
# 1. Версія ШІ краще обробляє великі літери з lower()
# 2. Обидві версії відсортовують літери, але моя версія не приводить слова до нижнього регістру
