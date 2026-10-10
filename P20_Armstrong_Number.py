# Program to check Armstrong number

num = int(input("Enter an integer: "))

original = num
digits = len(str(num))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

if original == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")