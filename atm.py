#==============================
# SIMPLE ATM SIMUALATOR
# =============================
def check_balance(balance):
    print(f"\nYour current balance is: ${balance:.2f}")

def deposit(balance, transactions):
    amount = float(input("Enter the amount to deposit: $"))
    if amount <= 0:
        print("Deposit amount must be greater than zero.")
        return balance
    balance += amount
    transactions.append(f"Deposited: ${amount:.2f}")
    print(f"Successfully deposited ${amount:.2f}.")
    return balance


def withdraw(balance, transactions):
    amount = float(input("Enter the amount to withdraw: $"))
    if amount <= 0:
        print("Withdrawal amount must be greater than zero.")
        return balance
    elif amount > balance:
        print("Insufficient balance.")
        return balance
    else:
        balance -= amount
        transactions.append(f"Withdrew: ${amount:.2f}")
        print(f"Successfully withdrew ${amount:.2f}.")
        return balance

def change_pin(current_pin):
    old_pin = input("Enter your current PIN: ")
    if old_pin != current_pin:
        print("Incorrect current PIN. PIN change failed.")
        return current_pin
    else:
        new_pin = input("Enter your new PIN: ")
        if len(new_pin) != 4  and not new_pin.isdigit():
            print("PIN must be a 4-digit number.")
            return current_pin
        confirm_pin = input("Confirm your new PIN: ")
        if new_pin != confirm_pin:
            print("PINs do not match. PIN change failed.")
            return current_pin
        print("PIN changed successfully.")
        new_pin = current_pin 
        return new_pin
    
def view_transactions(transactions):
    if len(transactions) == 0:
        print("No transactions available.")
    else:
        print("\nTransaction History:")
        print("---------------------")

        for transaction in transactions:
            print(transaction)

#====================
#MAIN PROGRAM
#====================
balance = 1000.00  # Initial balance
transactions = []  # List to store transaction history
current_pin = "1234"  # Default PIN

print("=============================")
print("WELCOME TO PYTHON ATM!")
print("=============================")

attempts = 3
while attempts > 0:
    entered_pin = input("Please enter your 4-digit PIN: ")
    if entered_pin == current_pin:
        print("PIN accepted. \nAccess granted.")
        while True:
            print("\nSelect an option:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. View Transaction History")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                check_balance(balance)
            elif choice == '2':
                balance = deposit(balance, transactions)
            elif choice == '3':
                balance = withdraw(balance, transactions)
            elif choice == '4':
                current_pin = change_pin(current_pin)
            elif choice == '5':
                view_transactions(transactions)
            elif choice == '6':
                print("Thank you for using Python ATM. \nGoodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect PIN. You have {attempts} attempts left.")
        else:
            print("Incorrect PIN. No attempts left.\nYOUR ACCOUNT HAS BEEN LOCKED!!!.")
