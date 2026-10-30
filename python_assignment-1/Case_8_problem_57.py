# Case 8 - Problem 57: Smart Canteen Order and Stock Management

items = ["Samosa", "Sandwich", "Coffee"]
prices = [20, 45, 25]
stock = [30, 15, 25]

total_sales = 0
n = int(input("Enter number of orders: "))

for i in range(n):
    print("Order", i + 1, "(0:Samosa, 1:Sandwich, 2:Coffee)")
    code = int(input("Enter item code: "))
    qty = int(input("Enter quantity: "))

    if code < 0 or code >= len(items) or qty <= 0:
        print("Invalid order input")
    elif qty <= stock[code]:
        bill = qty * prices[code]
        stock[code] = stock[code] - qty
        total_sales = total_sales + bill
        print(items[code], "x", qty, "-> Bill: Rs.", bill)
    else:
        print(items[code], "-> Rejected (Insufficient stock)")

print("Total Daily Sales: Rs.", total_sales)
print("Remaining Stock:")
for i in range(len(items)):
    print(items[i], ":", stock[i])
