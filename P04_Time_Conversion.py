# Convert seconds into hours, minutes and seconds

seconds = int(input("Enter time duration in seconds: "))

hours = seconds // 3600
seconds = seconds % 3600

minutes = seconds // 60
seconds = seconds % 60

print("Hours =", hours)
print("Minutes =", minutes)
print("Seconds =", seconds)