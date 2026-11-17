# AI log: none
class Safe:
    def __init__(self, code):
        self.__code = code

    def open(self, code):
        return code == self.__code

s = Safe("4821")
print(s.__dict__) # {'_Safe__code': '4821'}

s.__code = "0000"
print(s.open("4821"))
print(s.__dict__) # {'_Safe__code': '4821', '__code': '0000'}
# s.open("4821") поверне True, тому що зовнішнє присвоєння
# s.__code = "0000" створює окремий атрибут __code
# а не змінює початковий _Safe__code

