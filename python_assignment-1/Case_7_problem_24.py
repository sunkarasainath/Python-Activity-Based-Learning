# Case 7 - Problem 24: Courier Charge Optimization

weight = float(input("Parcel weight in kg: "))
length = float(input("Length in cm: "))
width = float(input("Width in cm: "))
height = float(input("Height in cm: "))
zone = int(input("Distance zone (1-3): "))
urgent = input("Urgent delivery? (yes/no): ").strip().lower()

if weight <= 0 or length <= 0 or width <= 0 or height <= 0:
    print("Invalid parcel details")
elif zone not in [1, 2, 3]:
    print("Invalid distance zone")
elif urgent not in ["yes", "no"]:
    print("Invalid urgency option")
else:
    standard = 40 + weight * 10 + zone * 10
    express = 70 + weight * 15 + zone * 15

    if urgent == "yes":
        express = express + 30

    if weight > 5:
        print("No service available for this weight")
    elif standard <= express:
        print("Selected service: Standard")
        print("Charge: Rs.", round(standard, 2))
    else:
        print("Selected service: Express")
        print("Charge: Rs.", round(express, 2))
