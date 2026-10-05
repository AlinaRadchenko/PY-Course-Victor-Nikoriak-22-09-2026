# AI log: none
# 1 спосіб:
list_num = []
for x in range(1,11):
    j = x ** 2
    t = (x, j)
    list_num.append(t)
print(list_num)

# 2 спосіб: List comprehension більш компактній та легший для читання
list_num = [(x, (x ** 2)) for x in range(1, 11)]
print(list_num)