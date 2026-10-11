# AI log: Розбирали, навіщо використовувати all() та чому перевірку типу
# потрібно виконувати перед перевіркою довжини

# Якщо спочатку перевіряти довжину, то len(12345) викличе TypeError,
# тому що int не підтримує len() і тоді спочатку ми перевіряємо тип

def arg_rules(type_, max_length, contains):
    def decorator(func):
        def wrapper(name):
            if type(name) != type_:
                print("Invalid type")
                result = False
            elif len(name) > max_length:
                print("Maximum length exceeded")
                result = False
            elif not all(i in name for i in contains):
                print("Required characters are missing")
                result = False
            else:
                result = func(name)
            return result
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('S@SH05'))
print(create_slogan(12345))

# Мій приклад
@arg_rules(type_=str, max_length=20, contains=[])
def favorite_movie(name):
    return f"My favorite movie is named {name}"

print(favorite_movie("Dune"))
print(favorite_movie("Supernatural"))
print(favorite_movie(123))