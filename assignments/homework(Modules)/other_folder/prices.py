# AI Log: використовувала, щоб зрозуміти роботу __name__ == "__main__",
# різницю між запуском файлу та імпортом модуля
def with_discount(price, percent):
    return round(price - (price * percent), 2)

def total(prices):
    sum_pr = sum(prices)
    return round(sum_pr, 2)


if __name__ == "__main__":

    print(with_discount(1200, 0.15))
    print(total([1200, 899, 450]))

# При запуску prices.py виводиться одна ціна зі знижкою та сума початкових цін
# а при запуску report.py ми вже виводимо ціни зі знижкою та їх суму