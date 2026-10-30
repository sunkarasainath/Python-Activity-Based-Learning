# Case 5 - Problem 15: Smart Parking Fee Management

entry = int(input("Entry hour (0-23): "))
exit_time = int(input("Exit hour (0-23): "))
vehicle = input("Vehicle (car/bike): ").strip().lower()

if entry < 0 or entry > 23 or exit_time < 0 or exit_time > 23:
    print("Invalid time")
elif exit_time <= entry:
    print("Invalid exit time")
elif vehicle not in ["car", "bike"]:
    print("Invalid vehicle")
else:
    duration = exit_time - entry
    if vehicle == "car":
        rate = 30
        maximum = 200
    else:
        rate = 15
        maximum = 100

    fee = duration * rate
    if fee > maximum:
        fee = maximum

    print("Parking duration:", duration, "hours")
    print("Parking fee: Rs.", fee)
