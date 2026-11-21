# AI log: отримала пояснення, чому Python може перебирати об'єкт без __iter__
# якщо в ньому реалізований __getitem__
class Sentence:
    def __init__(self, text):
        self.text = text.split()

    def __iter__(self):
        return iter(self.text)

    def __getitem__(self, index):
        return self.text[index]

    def __len__(self):
        return len(self.text)



s = Sentence("Python is fun")
print([word for word in s])   # ['Python', 'is', 'fun']
print([word for word in s])   # ['Python', 'is', 'fun']
print(s[0], s[-1], len(s))    # Python fun 3
print("is" in s)
print("")# True
try:
    s[10]
except IndexError as e:
    print(e)


for word in s:
    for word2 in s:
        print(word, word2)

print("")
# цикл for працює навіть без __iter__ в копії класу
# Python використовує механізм sequence fallback
# викликає __getitem__ з індексами коли виникає IndexError, Python розуміє, що елементи закінчилися
class SentenceWithoutIter:
    def __init__(self, text):
        self.text = text.split()

    def __getitem__(self, index):
        return self.text[index]

    def __len__(self):
        return len(self.text)

s2 = SentenceWithoutIter("Python is fun")
for word in s2:
    print(word)