#Практична робота
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students  #список
        self.teachers = []
        self.classes = []
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
    #1111
    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_class(self, class_obj):
        self.classes.append(class_obj)

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
my_school.expel_student(Student("Gleb", 100))
print("Оновлення")
for student in my_school.students:
    print(student)

#1
class Teacher:
    def __init__(self, name, subject, classes):
        self.name = name
        self.subject = subject
        self.classes = classes
#2
class Class:
    def __init__(self, number):
        self.number = number
        self.students = []
    def add_student(self, student):
        self.students.append(student)
