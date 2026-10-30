# Case 1 - Problem 7: Retail Billing with Multiple Discount Rules

n = int(input("Enter number of items: "))
subtotal = 0.0
valid = n > 0

for i in range(n):
    price = float(input("Enter price of item " + str(i + 1) + ": "))
    qty = int(input("Enter quantity of item " + str(i + 1) + ": "))
    if price <= 0 or qty <= 0:
        print("Invalid item details")
        valid = False
        break
    subtotal = subtotal + (price * qty)

if valid:
    if subtotal > 2000:
        discount = subtotal * 0.10
        if discount > 500:
            discount = 500.0
    else:
        discount = 0.0

    after_discount = subtotal - discount
    gst = after_discount * 0.05
    final_bill = after_discount + gst

    print("Subtotal: Rs.", round(subtotal, 2))
    print("Discount: Rs.", round(discount, 2))
    print("GST (5%): Rs.", round(gst, 2))
    print("Final Bill: Rs.", round(final_bill, 2))
