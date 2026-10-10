class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self,amount):
        if amount <= self._balance:
            self._balance -= amount
            print("Withdrawal of ",amount, "is successful!")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self._balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(400)
print("The account balance is: ", account.get_balance())
