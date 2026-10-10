# Program 29: Menu-driven mathematical application

while True:
    print("\n1. Check Prime")
    print("2. Check Palindrome")
    print("3. Check Armstrong")
    print("4. Factorial")
    print("5. Fibonacci Series")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter a number: "))
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        if n > 1 and count == 2:
            print("Prime Number")
        else:
            print("Not a Prime Number")

    elif choice == 2:
        n = int(input("Enter a number: "))
        if str(n) == str(n)[::-1]:
            print("Palindrome Number")
        else:
            print("Not a Palindrome Number")

    elif choice == 3:
        n = int(input("Enter a number: "))
        temp = n
        total = 0
        power = len(str(n))
        while temp > 0:
            digit = temp % 10
            total += digit ** power
            temp //= 10
        if n >= 0 and total == n:
            print("Armstrong Number")
        else:
            print("Not an Armstrong Number")

    elif choice == 4:
        n = int(input("Enter a number: "))
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        if n >= 0:
            print("Factorial =", fact)
        else:
            print("Factorial is not defined for negative numbers")

    elif choice == 5:
        n = int(input("Enter number of terms: "))
        a, b = 0, 1
        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()

    elif choice == 6:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice! Please try again.")
