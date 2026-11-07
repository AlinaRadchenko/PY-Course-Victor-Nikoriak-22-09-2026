# AI допоміг розібратися з атрибутами __name__, __doc__, co_nlocals та co_varnames.
def inspector(func):
    info = (f"Func name: {func.__name__}\n"
            f"Func docs: {func.__doc__}\n"
            f"Num of local variables: {func.__code__.co_nlocals}\n"
            f"Name of local variables: {func.__code__.co_varnames}\n")
    return info

def make_order(item, qty=1):
    """Creates an order and calculates its total price."""
    price = 100
    total = price * qty
    return f"{qty} x {item}: {total}"

# inspector(len) спричинить помилку AttributeError,
# тому,що ще вбудована функція len не має атрибута __code__.
# Помилка: AttributeError: 'builtin_function_or_method' object has no attribute '__code__'
print(inspector(make_order))
print(inspector(inspector))
print(inspector(len))