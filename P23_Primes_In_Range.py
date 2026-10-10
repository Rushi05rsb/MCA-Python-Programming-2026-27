
# Accept two integers representing a range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

count = 0

print("Prime numbers within the range are:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break7

        if is_prime:
            print(num, end=" ")
            count += 1

print("\nTotal number of prime numbers:", count)
