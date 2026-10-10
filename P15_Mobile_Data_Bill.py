data = float(input("Enter monthly data usage in GB: "))

if data <= 5:
    bill = 100
elif data <= 10:
    bill = 200
elif data <= 20:
    bill = 400
else:
    bill = 600

print("Total Bill =", bill)