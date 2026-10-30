# Case 2 - Problem 8: Manufacturing Cost and Profitability Analysis

material = float(input("Enter Material Cost: "))
labour = float(input("Enter Labour Cost: "))
machine = float(input("Enter Machine Cost: "))
units = int(input("Enter Units Produced: "))
sell_price = float(input("Enter Selling Price per Unit: "))

if material <= 0 or labour <= 0 or machine <= 0 or units <= 0 or sell_price <= 0:
    print("Invalid input values")
else:
    wastage = material * 0.05
    total_cost = material + labour + machine + wastage
    revenue = units * sell_price
    profit = revenue - total_cost
    profit_pct = (profit / total_cost) * 100

    if profit_pct >= 15:
        status = "Profit Target Achieved"
    else:
        status = "Below Profit Target"

    print("Total Production Cost: Rs.", round(total_cost, 2))
    print("Total Revenue: Rs.", round(revenue, 2))
    print("Net Profit: Rs.", round(profit, 2))
    print("Profit Percentage:", round(profit_pct, 2), "%")
    print("Status:", status)
