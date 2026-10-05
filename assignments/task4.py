#AI log: попросила підсказати, як рахувати повторення слів у словнику за допомогою get(),
# та придумати випадкове речення.
sentence = "Python makes coding fun Python helps beginners learn coding every day"
words = sentence.split()
print(words)
unique_words = {}
for word in words:
    unique_words[word] = unique_words.get(word, 0) + 1

print(unique_words)
