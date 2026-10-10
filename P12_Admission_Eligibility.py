# Program to check admission eligibility

maths = float(input("Enter Mathematics marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))

total = maths + physics + chemistry
percentage = total / 3

if maths >= 50 and physics >= 50 and chemistry >= 50 or percentage >= 60:
    print("Eligible for Admission")
else:
    print("Not Eligible for Admission")

print("Overall Percentage =", percentage)