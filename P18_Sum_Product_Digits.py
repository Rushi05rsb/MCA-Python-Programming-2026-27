# Program to find sum and product of digits

num = int(input("Enter an integer: "))

sum_digits = 0
product = 1

while num > 0:
    digit = num % 10
    sum_digits = sum_digits + digit
    product = product * digit
    num = num // 10

print("Sum of digits =", sum_digits)
print("Product of digits =", product)