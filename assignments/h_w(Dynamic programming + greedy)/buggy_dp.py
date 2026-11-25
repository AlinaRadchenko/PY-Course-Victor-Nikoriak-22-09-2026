# AI log: допоміг знайти та виправити помилку в min_coins
import functools

def stairs(n):
    """Ways to climb n stairs with steps of 1 or 2."""
    table = [0] * (n + 1)
    # Bug 1: список створений недостатнього розміру table = [0] * n
    table[0] = 1
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]

        # table[i] = table[i - 1] + table[i - 2]
        #     ~~~~~^^^
        # IndexError: list assignment index out of range
    return table[n]


def min_coins(amount, coins):
    """Smallest number of coins that add up to amount, or None if it is impossible."""
    best = [0] + [float("inf")] * amount
    # Bug 2: ми ще не знаємо, скільки монет потрібно для кожної суми
    # тому не можемо одразу записувати 0 best = [0] * (amount + 1)
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and best[a - c] + 1 < best[a]:
                best[a] = best[a - c] + 1
    return best[amount] if best[amount] != float("inf") else None



@functools.cache
def ways(n, steps):
    """Ways to climb n stairs if one step can be any number from steps."""
    if n == 0:
        return 1
    if n < 0:
        return 0
    return sum(ways(n - s, steps) for s in steps)


if __name__ == "__main__":
    print(stairs(5))
    print(min_coins(6, [1, 3, 4]))
    print(ways(10, (1, 2))) # Bug 2: cписок не можна використовувати як ключ кешу
    #  print(ways(10, [1, 2]))
    #  ~~~~^^^^^^^^^^^^
    # TypeError: unhashable type: 'list'