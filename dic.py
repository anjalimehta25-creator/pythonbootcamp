Prices = {
    "apple": 50,
    "banana": 30,
    "milk": 60,
    "bread": 40,
    "eggs": 80
}

out_of_stock = {"milk", "eggs"}

Order = ["apple", "milk", "bread", "banana"]

total = 0

for item in Order:
    if item in out_of_stock:
        print(item, "is unavailable")
    else:
        total += Prices[item]

print("Final order value:", total)