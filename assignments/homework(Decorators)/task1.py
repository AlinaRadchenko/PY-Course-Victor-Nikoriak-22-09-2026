# AI log: none
def get_greeter():
    def greeter(name):
        return f"Hi, {name}!"
    return greeter



# Перший виклик виведе саму функцію, бо ми нічого не передали
# Другий виведе привітання, бо ми передаємо аргумент до внутрішній функції
print(get_greeter())
print(get_greeter()("Olena"))