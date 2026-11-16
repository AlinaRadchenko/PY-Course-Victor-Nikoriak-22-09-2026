# AI log:
# Використала для допомоги з побудовою логіки перевірки email, розбору помилок та перевірка коду
# за допомогою асистента виправлено логічні помилки та уточнено розташування перевірок
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        if not self.validate(email):
            raise ValueError("Invalid email")

# обрала staticmethod бо метод працює лише з переданим email
    @staticmethod
    def validate( email):
        if isinstance(email, str) and email.count("@") == 1:
            login, domain = email.split("@")

            if login and domain:
                if login[0].isalnum() and login[-1].isalnum():

                    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.-"
                    if any (char not in allowed for char in login):
                        return False

                    if any(not login[i].isalnum() and not login[i + 1].isalnum() for i in range(len(login) - 1)):
                        return False

                    if domain.count(".") < 1:
                        return False

                    parts = domain.split(".")

                    if any(not part for part in parts):
                        return False

                    allowed_domain = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-."

                    if any(char not in allowed_domain for char in domain):
                        return False

                    for part in parts:
                        if not part[0].isalnum() or not part[-1].isalnum():
                            return False

                    if len(parts[-1]) < 2:
                        return False

                    if any(not domain[i].isalnum() and not domain[i + 1].isalnum() for i in range(len(domain) - 1)):
                        return False

                    return True

        return False

assert User.validate("abc.def@mail.com") is True
assert User.validate("abc-@mail.com") is False
assert User.validate("abc..def@mail.com") is False
assert User.validate("abc.def@mail.c") is False

User("Ira", "ira@@mail.com")  # ValueError

