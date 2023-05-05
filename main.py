#4
class Bank:
    def __init__(self, customer, blnce):
        self.customer = customer
        self.blnce = blnce
class BankAccount:
    def __init__(self, customers, balance):
        self.customers = customers
        self.balance = balance
    def get_total_balance(self, blnce, balance):
        x =  blnce + balance
        return x
name = Bank("Zhenia", 1000)
name1 = Bank("Zahar", 600)
name2 = Bank("Sasha", 180)

print(f"Клієнт: {name.customer}, Баланс {name.blnce} грн")
print(f"Клієнт: {name1.customer}, Баланс {name1.blnce} грн")
print(f"Клієнт: {name2.customer}, Баланс {name2.blnce} грн")
print("-------------------------------------")
name_res = BankAccount("Gleb", 120)
print(f"Новий клієнт: {name_res.customers}, Баланс {name_res.balance} грн")
print("-------------------------------------")
print(f"Загальний баланс усіх клієнтів становить: {name_res.get_total_balance(blnce = 1780, balance = 120)} грн")

