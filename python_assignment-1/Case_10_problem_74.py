# Case 10 - Problem 74: Campus Festival Registration and Financial Audit

fee = float(input("Enter Registration Fee per Student: "))
sponsorship = float(input("Enter Sponsorship Amount: "))
expenses = float(input("Enter Total Festival Expenses: "))

participants = ["STU101", "STU102", "STU103", "STU101", "STU104", "STU102"]

if fee < 0 or sponsorship < 0 or expenses < 0:
    print("Invalid financial inputs")
else:
    unique_list = []
    duplicates = []

    for pid in participants:
        if pid in unique_list:
            duplicates.append(pid)
        else:
            unique_list.append(pid)

    reg_income = len(unique_list) * fee
    total_income = reg_income + sponsorship
    balance = total_income - expenses

    print("Unique Participants:", len(unique_list))
    print("Duplicate Entries Detected:", duplicates)
    print("Registration Revenue: Rs.", round(reg_income, 2))
    print("Total Festival Income: Rs.", round(total_income, 2))
    print("Final Financial Balance: Rs.", round(balance, 2))
