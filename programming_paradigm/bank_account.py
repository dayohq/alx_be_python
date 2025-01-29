class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
            """Add the specified amount to the account balance."""
            if amount > 0:
                self.__account_balance += amount
                return self.display_balance() # Return the formatted balance after deposit
            return "Deposit amount must be greater than zero."
        
    def withdraw(self, amount):
            """
            Deduct the specified amount from the account balance if funds are sufficient. 
            Return True if the transaction is successful, otherwise False.
            """
            if 0 < amount <= self.__account_balance:
                self.__account_balance -= amount
                return self.display_balance() # Return the formatted balance after deposit
            return "Withdrawal amount must be greater than zero."
        
    def display_balance(self):
            """Return the current account balance."""
            return f"Current Balance: ${self.__account_balance:.2f}"