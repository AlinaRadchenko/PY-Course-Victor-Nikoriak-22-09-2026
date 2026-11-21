# AI log: допоміг розібратися з перевірками генератора
def averager():
    total = 0.0
    count = 0
    avg = None
    try:
        while True:
            value = yield avg
            if value is not None:
                total += value
                count += 1
                avg = total / count
    finally:
        print(f"Closed after {count} numbers, average {avg}")


avg = averager()
next(avg)             # запускає генератор
print(avg.send(10))   # 10.0
print(avg.send(20))   # 15.0
print(avg.send(60))   # 30.0
avg.close()           # Closed after 3 numbers, average 30.0
print("")
avg = averager()
next(avg)
avg.close()
print("")
# генератор не запускається
avg = averager()
avg.close()
# send(10) передає число в генератор, який ще не дійшов до першого yield
# тому виникає помилка TypeError: can't send non-None value to a just-started generator
try:
    avg = averager()
    print(avg.send(10))
except TypeError as e:
    print(e)

# finally виводить повідомлення, коли закриваємо запущений генератор
# якщо генератор ще не запускався, finally не виконується