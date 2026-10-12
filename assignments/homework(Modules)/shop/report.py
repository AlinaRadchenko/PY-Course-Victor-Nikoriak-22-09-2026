# блок if __name__ == "__main__": у prices.py не буде виконано
# так, як він запускається тільки коли ми запустимо prices.py напряму
import sys
sys.path.insert(0, "../other_folder")

from prices import with_discount
from prices import total


prices = [1200, 899, 450]
discounted_prices = []
for price in prices:
    result = with_discount(price, 0.15)
    discounted_prices.append(result)

print(discounted_prices)
print(total(discounted_prices))