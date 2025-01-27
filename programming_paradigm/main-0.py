import sys
from bank_account import BankAccount

def main():
    # Create an instance of BankAccount with a default initial balance
    account = BankAccount()

    # Check if the user provided a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python main-0.py [operation:amount or display]")
        return
    
    # Parse the operation and amount from the command-line argument
    operation = sys.argv[1]

    if operation.startswith("deposit:"):
        try:
            amount = float(operation.split(":")[1])
            if account.deposit(amount):
                print(f"Deposited: ${amount:.2f}")
            else:
                print("Invalid deposit amount.")
        except ValueError:
            print("Invalid amount. Please provide a valid number.")

    elif operation.startswith("withdraw:"):
        try:
            amount = float(operation.split(":")[1])
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds or invalid withdrawal amount.")
        except ValueError:
            print("Invalid amount. Please provide a valid number.")

    elif operation == "display":
        print(account.display_balance())

    else:
        print("Invalid operation. Supported operations: deposit:[amount], withdraw:[amount], display.")

if __name__ == "__main__":
    main()