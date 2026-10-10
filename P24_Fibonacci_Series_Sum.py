n = int(input("Enter number of terms: "))

a = 0
b = 1
total = 0

print("Fibonacci series:")

for i in range(n):
    print(a, end=" ")
    total += a
    a, b = b, a + b

print("\nSum of series:", total)
