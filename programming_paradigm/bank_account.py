class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.balance = float(initial_balance)

    def deposit(self, amount):
        self.balance += float(amount)

    def withdraw(self, amount):
        amount = float(amount)
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
