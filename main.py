import random
class Animal:
    def __init__(self , name, age, species, health , hunger , happiness):
        self.species = species
        self.name = name
        self.age = age
        self.health = health
        self.hunger = hunger
        self.happiness = happiness
    def grow(self):
        self.age += 1
        self.healt = random.randint(1 , 10)
        self.hunger = random.randint(1, 20)
        self.happiness = random.randint(1, 100)
    def eat(self):
        if self.hunger >= 10:
            self.healt += random.randint(0 , 7)
            self.happiness += random.randint(0 , 7)
            self.hunger -= random.randint(5, 8)
        else:
            print("Тваринка не голодна")
    def play(self):
        if self.happiness <= 60:
            self.happiness += random.randint(10, 20)
        else:
            print("Тваринка досить весела")
    def __str__(self):
        return f"Тваринка {self.name}, характеристика: " \
               f"\nВік: {self.age} " \
               f"\nВид {self.species}" \
               f"\nСтан здоров'я {self.health}" \
               f"\nСитість {self.hunger}" \
               f"\nНастрій {self.happiness}"
class Zoo():
    def __init__(self, name, animals):
        self.animals = animals
        self.name = name
        super().__init__()
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'{animal.name} був доданий до зоопарку {self.name}')
    def remove_animal(self, animal):
        expelled_animals = next(filter(lambda s: s.name == animal.name and
                                                 s.species == animal.species and
                                                 s.age == animal.age and
                                                 s.happiness == animal.happiness and
                                                 s.happiness == animal.happiness and
                                                 s.happiness == animal.happiness, self.animals), None)
        if expelled_animals is not None:
            self.animals.remove(expelled_animals)
            print(f'{expelled_animals.name} був видалений з {self.name}')
        else:
            print(f'{animal.name} nе було знайдено в {self.name}')

    def feed_all(self, animal):
        animal.hunger += random.randint(5,10)
    def play_with(self, animal):
        animal.happiness += random.randint(30,60)
    def grow_all(self, animal):
        animal.age += 1
    def __str__(self):
        return super().__str__() + f"Характеристика покращилась!"

animal1 = Animal("Жираф", 12, "В крапочку", 10, 12, 45)
animal2 = Animal("Лев", 5, "Королевький", 15, 25, 40)
animal3 = Animal("Мавпа", 7, "Буффа", 10, 15, 77)
animal4 = Animal("Слон", 10, "Великий", 7, 25, 30)

my_zoo = Zoo("Зоопарк!!!", [animal1, animal2, animal3, animal4])
print("Початковий список:")
for animal in my_zoo.animals:
    print(animal)


my_zoo.add_animal(Animal("Тигр", 2, "полосатий", 20, 20, 70))
print("Оновлення")
for animal in my_zoo.animals:
    print(animal)


with open("student_info.txt", "w") as file:
    for day in range(1, 11):
        file.write(str(my_zoo.animals))