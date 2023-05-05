#3
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
name = Car(brand = "Lamborghini",
           model = "Huracan",
           year = 2014)
print(f"Марка: {name.brand}")
print(f"Модель: {name.model}")
print(f"Рік: {name.year}")
