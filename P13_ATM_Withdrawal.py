# Program to simulate ATM withdrawal

pin = int(input("Enter PIN: "))
balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

if pin != 1234:
    print("Invalid PIN")
elif amount <= 0:
    print("Invalid withdrawal amount")
elif amount > balance:
    print("Insufficient balance")
else:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance =", balance)