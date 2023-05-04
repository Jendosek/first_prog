#   classes
class Student:
    print("Hi!")
    def __init__(self, height = 150):
        self.height = height
        self.text = "I`m shy"
oleg = Student() #Обєкт екземпляру класу
print(oleg.height)
masha = Student(height=200)
print(masha.height)