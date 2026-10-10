# Program 21: Number guessing game

secret_number = 42
print("Guess the secret number.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print("Correct! You found the number.")
        break
