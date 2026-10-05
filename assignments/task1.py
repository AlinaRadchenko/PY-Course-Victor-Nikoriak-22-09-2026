# AI log: none
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
# Вартість апельсинів очікую 48.0
for item in stock:
    total_sum = stock[item] * prices[item]
    print(f"Total price {item}: {total_sum}")
