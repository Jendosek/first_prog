#4
class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner
    def deposit(self, all):
        self.all = all
    def withdraw(self, dep):
        self.dep = dep
name = BankAccount(balance=1000, owner=100)
print(name.all)

