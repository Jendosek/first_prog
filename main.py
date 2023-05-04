#   classes
class Student:
    print("Hi!")
    count = 0
    def __init__(self, height = 150):
        self.height = height
        self.text = "I`m shy"
        Student.count += 1
    def brething(self, height):
        return self.height - 10
oleg = Student() #Обєкт екземпляру класу
print(oleg.height)
masha = Student(height=200)
print(masha.height)
print(Student.count)
print(masha.brething(None))