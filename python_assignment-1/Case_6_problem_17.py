# Case 6 - Problem 17: Student Performance Trend Analysis

name = input("Student name: ")
subjects = ["Python", "Mathematics", "English"]
total = 0
valid = True

for subject in subjects:
    print(subject)
    old = int(input("Earlier marks: "))
    new = int(input("Latest marks: "))
    if old < 0 or old > 100 or new < 0 or new > 100:
        valid = False
        print("Invalid marks")
        break

    change = new - old
    total = total + new
    print("Change:", change)
    if new < 40:
        print("Weak subject")
    else:
        print("Subject pass level reached")

if valid:
    average = total / len(subjects)
    if average >= 75:
        result = "Good"
    else:
        result = "Needs Improvement"
    print("Average:", round(average, 2))
    print("Performance:", result)
