# AI log: використала для пояснення логіки програми та підказати, як правильно тут використовувати get() і цикли
stock = {
    "milk": 12,
    "bread": 8,
    "cheese": 5,
    "eggs": 0,
    "coffee": 14,
    "rice": 20
}

prices = {
    "milk": 2.5,
    "bread": 1.8,
    "cheese": 6,
    "eggs": 3.2,
    "coffee": 8.5,
    "rice": 2.2
}
print("Choose a product:")
print("If you're finished, type 'done'")
for name in stock:
    print(f"|{name}", sep="|", end="|")

cart = {}
while True:
    products = input("\nProduct--> ").lower()
    if products == "done":
        break

    if products not in stock:
        print("This product is not available")
        continue

    quantity = int(input("\nQuantity--> "))
    if quantity > stock.get(products) or quantity < 1:
        print("The required quantity is not available")
        continue

    cart[products] = cart.get(products, 0) + quantity
    stock[products] = stock.get(products,0) - quantity

total = 0
for product, quantity in cart.items():
    cost = quantity * prices[product]
    total += cost
    print(f"Product: {product} | Quantity: {quantity} | Price: ${prices[product]:.2f} | Cost: ${cost:.2f}")
print(f"Total: ${total:.2f}")

out_of_stock = [name for name in stock if stock[name] == 0]
print(out_of_stock)
