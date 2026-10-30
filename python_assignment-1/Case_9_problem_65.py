# Case 9 - Problem 65: Campus Resource Allocation Under Constraints

available = int(input("Enter Total Available Projectors: "))
n = int(input("Enter Number of Activities: "))

if available < 0 or n <= 0:
    print("Invalid input")
else:
    total_shortage = 0
    for i in range(n):
        act_name = input("Enter Activity " + str(i + 1) + " Name: ")
        req = int(input("Requested Projectors: "))

        if req <= available:
            alloc = req
            shortage = 0
        else:
            alloc = available
            shortage = req - alloc

        available = available - alloc
        total_shortage = total_shortage + shortage
        print(act_name, "-> Requested:", req, "| Allocated:", alloc, "| Shortage:", shortage)

    print("Total Equipment Shortage:", total_shortage)
    print("Projectors Remaining:", available)
