# Case 4 - Problem 39: Multi-Stage Examination Eligibility System

attendance = float(input("Enter Attendance Percentage: "))
internal = float(input("Enter Internal Marks (0-100): "))
lab_done = input("Lab Completed? (yes/no): ").strip().lower()
fee_paid = input("Fee Cleared? (yes/no): ").strip().lower()

if attendance < 0 or attendance > 100 or internal < 0 or internal > 100:
    print("Invalid input values")
else:
    unmet = []
    if attendance < 75:
        unmet.append("Attendance below 75%")
    if internal < 40:
        unmet.append("Internal marks below 40")
    if lab_done != "yes":
        unmet.append("Laboratory work incomplete")
    if fee_paid != "yes":
        unmet.append("Tuition fee not cleared")

    if len(unmet) == 0:
        print("Result: ELIGIBLE for Final Examination")
    else:
        print("Result: NOT ELIGIBLE")
        print("Unmet Requirements:")
        for reason in unmet:
            print("-", reason)
