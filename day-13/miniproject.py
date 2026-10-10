class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self.amount = amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print("You have successfully withdrawn ksh. ", amount)
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self._balance

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print("You have successfully withdrawn ksh. ", amount, "from saving account")
        else:
            print("Insufficient funds!")

class CurrentAccount(BankAccount):
    def __init__(self, owner, balance, overdraft):
        super().__init__(owner, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= self._balance + self.overdraft:
            self._balance -= amount
            print("You have successfully withdrawn ksh. ", amount, "from your current account")
        else:
            print("Insufficient funds!")

savings = SavingsAccount("Wilfred ", 1000)
current = CurrentAccount("Wilfred ", 1000, 500)

accounts = [savings, current]
for account in accounts:
    account.withdraw(1200)
    print("Balance: ", account.get_balance())
