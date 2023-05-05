#1
class Person:
    def __init__(self, name):
        self.name = name
    def is_adult(self, age):
        if 0 < age <= 18:
            print("False (Менше 18 років)")
        else:
            print("True (Більше 18 років)")
result = Person(name = "Zhenia")

print(f"Ім'я: {result.name}")
result.is_adult(20)
