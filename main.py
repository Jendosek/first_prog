#restaurant simulator
class FoodItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class Menu():
    def __init__(self, iteams):
        self.items = iteams
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        self.items.remove(item)
    def menu(self):
        for item in self.items:
            print(item.name + " - " + item.description + " - $" + str(item.price))
class Order:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        self.items.remove(item)
    def total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

class Restaurant(Menu):
    def __init__(self, menu):
        super().__init__(self)
        self.menu = menu
        self.orders = []
    def new_menu(self):
        self.menu.display_menu()
    def place_order(self, order):
        self.orders.append(order)
    def remove_order(self, order):
        self.orders.remove(order)
    def display_orders(self):
        for order in self.orders:
            for item in order.items:
                print(item.name + " - $" + str(item.price))
            print("Total: $" + str(order.calculate_total()) + "\n")

#вивід

with open("orders.txt", "w") as file:
    file.write("Order #" + str())
    for item in ...:
        file.write(item.name + " - $" + str(item.price))

