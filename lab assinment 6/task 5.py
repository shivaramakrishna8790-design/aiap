class BankAccount:
    # Constructor to initialize account holder and balance
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance!")

    # Method to display current balance
    def display_balance(self):
        print(f"Account Holder: {self.name}, Balance: {self.balance}")

# Example usage
acc = BankAccount("Anvesh", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.display_balance()
