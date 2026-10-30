# Case 3 - Problem 18: Fuel Consumption and Route Comparison

distance = float(input("Enter Trip Distance (km): "))
fuel_price = float(input("Enter Fuel Price per Litre: "))

vehicles = [
    ("Hatchback", 20.0),
    ("Sedan", 15.0),
    ("SUV", 12.0)
]

if distance <= 0 or fuel_price <= 0:
    print("Invalid trip inputs")
else:
    best_vehicle = ""
    min_cost = -1.0

    for v in vehicles:
        v_name, mileage = v
        fuel_needed = (distance / mileage) * 1.10
        cost = fuel_needed * fuel_price
        print(v_name, "-> Fuel:", round(fuel_needed, 2), "L | Cost: Rs.", round(cost, 2))

        if min_cost < 0 or cost < min_cost:
            min_cost = cost
            best_vehicle = v_name

    print("Lowest Cost Option:", best_vehicle, "at Rs.", round(min_cost, 2))
