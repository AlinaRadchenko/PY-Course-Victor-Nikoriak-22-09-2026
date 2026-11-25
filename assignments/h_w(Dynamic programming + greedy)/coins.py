# AI log: використовувала для пояснення завдання та перевірки коду
# отримала підказки для написання min_coins і порівняння
# greedy алгоритму з динамічним програмуванням

def make_change(amount, coins=(1, 2, 5, 10, 20, 50)):
    result = []

    for c in sorted(coins, reverse=True):
        while amount >= c:
            result.append(c)
            amount -= c

    return result if amount == 0 else None

def min_coins(amount, coins):
    best = [0] + [float("inf")] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and best[a - c] + 1 < best[a]:
                best[a] = best[a - c] + 1
    return best[amount] if best[amount] != float("inf") else None


assert min_coins(6, [1, 3, 4]) == 2
assert min_coins(68, [1, 2, 5, 10, 20, 50]) == 5
assert min_coins(3, [2, 5]) is None
assert min_coins(0, [1]) == 0

for amount in range(1, 31):
    greedy = make_change(amount, [1, 3, 4])
    optimal = min_coins(amount, [1, 3, 4])

    if len(greedy) > optimal:
        # дивимося для якого числа, greedy використав більше монет
        print(amount, len(greedy), optimal)

# greedy алгоритм обирає найбільшу монету на кожному кроці
# не думаючи про оптимальний варіант