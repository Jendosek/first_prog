#///classes///dubl_2
#1  симулятор навчального закладу
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students  #список
    def admit_student(self, student):
        self.students.append(student)
        print(f'{student.name} був допущений до школи {self.name}')
    def expel_student(self, student):
        expelled_student = next(filter(lambda s: s.name == student.name and
                                                 s.grade == student.grade, self.students), None)
        if expelled_student is not None:
            self.students.remove(expelled_student)
            print(f'{expelled_student.name} був видалений з {self.name}')
        else:
            print(f'{student.name} е було знайдено в {self.name}')

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def promote(self):
        self.grade += 1
        print(f'{self.name} був підвищений {self.grade}')
    def demote(self):
        self.grade -= 1
        print(f'{self.name} був понижений за гру в шахи {self.grade}')
    def __str__(self):
        return f'{self.name} - Ранг {self.grade}'

lisa = Student("Alisa", 6)
masha = Student("Maria", 2)
andriiko = Student("Andriy", 50)
volodumer = Student("Volodya", 23)
gleb = Student("Gleb", 100)

my_school = School("ItStep", [lisa, masha, andriiko, volodumer, gleb])
print("Початкові студенти")
for student in my_school.students:
    print(student)

my_school.admit_student(Student("Zhenia", 77))
my_school.expel_student(Student("Volodya", 23))
print("Оновлення")
for student in my_school.students:
    print(student)



"""multiply = lambda x, y: x*y
print(multiply(2,5))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_numbers = list(filter(lambda a: a % 2 == 0, numbers))
print(filtered_numbers)"""
