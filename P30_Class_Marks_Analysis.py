# Program 30: Analyze marks of N students

n = int(input("Enter number of students: "))

marks = []
total = 0
passed = 0
failed = 0
above_75 = 0

for i in range(n):
    m = float(input("Enter marks: "))
    marks.append(m)
    total += m

    if m >= 40:
        passed += 1
    else:
        failed += 1

    if m > 75:
        above_75 += 1

average = total / n

print("Class Average:", average)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Passed Students:", passed)
print("Failed Students:", failed)
print("Students Scoring Above 75%:", above_75)
