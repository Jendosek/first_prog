#1
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
print_info = Student(name="Zhenia", age = 16)
print(f"Ім`я студента: {print_info.name}")
print(f"Вік студента: {print_info.age} років")
