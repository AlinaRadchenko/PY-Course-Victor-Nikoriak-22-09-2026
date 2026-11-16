# AI log: пояснення логіки переміщення працівників між керівниками
# також для пошуку помилок та перевірки реалізованого коду
class Boss:
    def __init__(self, id_, name, company):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def add_worker(self, worker):
        if not isinstance(worker, Worker):
            raise TypeError
        worker.boss = self

    @property
    def workers(self):
        return tuple(self._workers)

    def __repr__(self):
        return f"Boss({self.id}, {self.name}, {self.company})"


class Worker:
    def __init__(self, id_, name, company, boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss



    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if not isinstance(new_boss, Boss):
            raise TypeError

        if new_boss is self._boss:
            return

        if self._boss is not None:
            self._boss._workers.remove(self)

        self._boss = new_boss
        new_boss._workers.append(self)

    def __repr__(self):
        return (
            f"Worker({self.id}, {self.name!r}, "
            f"{self.company!r}, boss={self.boss.name!r})"
        )


anna = Boss(1, "Anna", "Beetroot")
ira = Worker(10, "Ira", "Beetroot", anna)
oleh = Boss(2, "Oleh", "Beetroot")

oleh.add_worker(ira)

print(anna.workers)
print(oleh.workers)
print(ira)

ira.boss = oleh
print(oleh.workers)


# 1. повторення: використання @property та @setter,
# нове: взаємопов'язана робота двох класів Boss і Worker,
# та використання tuple для захисту внутрішнього списку.

# 2. якщо повернути звичайний список, зовнішній код зможе, додавати або видаляти
# працівників в обхід перевірок і setter

# 3. спочатку перевіряємо, чи є новий керівник екземпляром Boss
# якщо перевірка не пройдена, викликається TypeError та працівник
# залишається у списку старого керівника та його поточний зв'язок не змінюється
