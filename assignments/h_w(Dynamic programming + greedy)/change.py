# AI log: none
def make_change(amount, coins=(1, 2, 5, 10, 20, 50)):
    result = []

    for c in sorted(coins, reverse=True):
        while amount >= c:
            result.append(c)
            amount -= c

    return result if amount == 0 else None


# make_change(6, (1, 3, 4))
# Результат greedy алгоритму, [4, 1, 1] - 3 монети
# Краще рішення, [3, 3] - 2 монети

assert make_change(68) == [50, 10, 5, 2, 1]
assert make_change(0) == []
assert make_change(7, (2, 5)) == [5, 2]
assert make_change(3, (2, 5)) is None