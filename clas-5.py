class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds. Cannot withdraw more than the available balance.")
        else:
            print("Invalid withdrawal amount. Please withdraw a positive amount.")


account = Account("John Doe", 1000)


account.deposit(500)
account.withdraw(300)
account.withdraw(800)  


print(f"Final balance for {account.owner}: ${account.balance}")

