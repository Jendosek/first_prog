#4
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def add_customer(self, customer):
        self.customer = customer

result = Bank("Zhenia", 1000)
print(result.name)
print(result.balance)
result.add_customer("dod")


