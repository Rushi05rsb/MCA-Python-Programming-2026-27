# Program 25: Display all factors and count them

n = int(input("Enter an integer: "))
count = 0

print("Factors are:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
        count += 1

print("\nTotal number of factors:", count)