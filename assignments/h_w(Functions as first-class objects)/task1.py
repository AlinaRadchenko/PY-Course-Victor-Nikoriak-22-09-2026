# AI log: none
def count_locals(func):
    return func.__code__.co_nlocals

def make_order(item, qty=1):
    price = 100
    total = price * qty
    return f"{qty} x {item}: {total}"

# co_nlocals порахує кількість локальних змінних - 4,
# co_varnames виводе імена локальних змінних item, qty, price, total

print(count_locals(make_order))