# AI log: допоміг розібратися з логікою генераторів та перевірити код
# також для пояснення перевірок
import sys
import os
import tracemalloc

from itertools import islice, groupby
from contextlib import closing
# Seed: 4821
def read_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")


def parse(lines):
    for line in lines:
        parts = line.split()

        if len(parts) != 6:
            continue
        time, ip, method, path, status, ms = parts
        try:
            status = int(status)
            ms = int(ms)
        except ValueError:
            continue

        yield {
            "time": time,
            "ip": ip,
            "path": path,
            "status": status,
            "ms": ms}

def errors(records):
    for record in records:
        if record["status"] >= 500:
            yield record

# Перші п'ять помилок
with closing(read_lines("access.log")) as lines:
    records = parse(lines)
    error_records = errors(records)

    for record in islice(error_records, 5):
        print(record["time"], record["path"])

print("")
# Підрахунок записів за першими трьома годинами
with closing(read_lines("access.log")) as lines:
    records = parse(lines)

    hours = groupby(records, key=lambda record: record["time"][:13])

    for hour, group in islice(hours, 3):
        count = sum(1 for _ in group)
        print(hour, count)

print("")
# Вимірювання пам'яті для перших п'яти помилок
tracemalloc.start()

with closing(read_lines("access.log")) as lines:
    first = list(islice(errors(parse(lines)), 5))

current, peak_errors = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("First five errors:", peak_errors // 1024, "KiB")
# Окреме вимірювання пам'яті для readlines()
tracemalloc.start()

with open("access.log", "r", encoding="utf-8") as f:
    all_lines = f.readlines()

current, peak_readlines = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("readlines():", peak_readlines // 1024, "KiB")

del all_lines

print("Python version:", sys.version)
print("File size:", os.path.getsize("access.log"), "bytes")

# однакові години йдуть поруч, тому що записи створюються в хронологічному порядку
# кщо перемішати рядки, записи однієї години можуть опинитися в різних групах.
# Сортування всього файлу в пам'яті потребувало б зберігання всіх записів одночасно.
# readlines() зберігає всі рядки у списку, тому використовує більше пам'яті.