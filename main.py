"""# super()

#1
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} кушає")
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def bark(self):
        print(f"{self.name} гавкає")

class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def bark(self):
        print(f"{self.name} мяукає")
dog1 = Dog("Denis", 5, "buldog")
print(f"Ім'я собаки: {dog1.name}")
print(f"Вік собакu: {dog1.age}")
print(f"Порода собаки: {dog1.breed}")
dog1.eat()
dog1.bark()

print()

cat1 = Cat("Tima", 10, "british")
print(f"Ім'я кота: {cat1.name}")
print(f"Вік кота: {cat1.age}")
print(f"Порода кота: {cat1.breed}")
cat1.eat()
cat1.bark()"""



#2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, age: {self.age},"
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def  __str__(self):
        return super().__str__() + f" Student_ID: {self.student_id}"

student1 = Student("Zhenia", 16, "95dr645h56")
with open("student_info.txt", "w") as file:
    file.write(str(student1))