
# Accept marks for five subjects
marks1 = float(input("Enter marks of Java: "))
marks2 = float(input("Enter marks of Python: "))
marks3 = float(input("Enter marks of COA: "))
marks4 = float(input("Enter marks of ADBMS: "))
marks5 = float(input("Enter marks of Web Development: "))

# Calculate total marks
total = marks1 + marks2 + marks3 + marks4 + marks5

# Calculate average marks
average = total / 5

# Calculate percentage (assuming each subject is out of 100)
percentage = (total / 500) * 100

# Display results
print("Total Marks =", total)
print("Average Marks =", average)
print("Percentage =", percentage, "%")