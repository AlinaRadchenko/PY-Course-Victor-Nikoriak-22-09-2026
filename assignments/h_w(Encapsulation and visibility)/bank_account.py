# AI log: допомога з перевіркою початкового балансу та правильним записом умов
# перевірка помилок і тестування класу
import math
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance
        if self._balance != 0:
            self._check_amount(balance)


    @property
    def balance(self):
        return self._balance


    def _check_amount(self, amount):
        if not (not isinstance(amount, bool) and isinstance(amount, (int, float))  and amount > 0 and math.isfinite(amount)):
            raise ValueError


    def deposit(self, amount):
        self._check_amount(amount)
        self._balance += amount


    def withdraw(self, amount):
        self._check_amount(amount)
        if self._balance >= amount:
            self._balance -= amount
        else:
            raise ValueError(f"Insufficient funds. Available balance: {self._balance}")


acc = BankAccount("Ira")
print(acc.balance)  # 0

acc = BankAccount("Ira", 100)
acc.deposit(50)
acc.withdraw(30)
print(acc.balance)  # 120


# acc._balance = 1000
# print(acc.balance)
# очікую, що значення зміниться, тому що _balance є звичайним
# внутрішнім атрибутом, до якого ми звернулися напряму


# acc.balance = 1000
# Error: ми створили balance — read-only property без setter, тому не можемо змінювати
# AttributeError: property 'balance' of 'BankAccount' object has no setter