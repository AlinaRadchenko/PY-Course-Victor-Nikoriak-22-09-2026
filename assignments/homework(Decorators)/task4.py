# AI log: не розуміла, як будувати ієрархію вкладених функцій у декораторі з параметрами
# думала, що декоратор завжди є першою функцією, тому розбирали різницю між звичайним декоратором і декоратором із параметрами
def stop_words(lst):
    def decorator(func):
        def wrapper(name):
            result = func(name)
            for i in lst:
                result = result.replace(i, "*")
            return result
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


# create_slogan("BMW") очікую повернення * drinks * in his brand new *!
# create_slogan("Pepsi") очікую повернення "Pepsi drinks * in his brand new *!"
print(create_slogan("Steve"))
print(create_slogan("BMW"))
print(create_slogan("Pepsi"))