# Program 26: Calculate GCD and LCM using iterative statements

a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))

gcd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

lcm = (a * b) // gcd

print("GCD =", gcd)
print("LCM =", lcm)
