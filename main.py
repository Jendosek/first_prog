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
    #3
    def get_school_statistics(self):
        total_students = len(self.students)
        if total_students == 0:
            avg_grade = 0
        else:
            avg_grade = sum(student.grade for student in self.students) / total_students
        return f"На {total_students} студентів середня оцінка по школі {avg_grade}"

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
    #3
    def add_student(self, student):
        self.students.append(student)
    def get_average_grade(self):
        total_grade = 0
        for student in self.students:
            total_grade += student.grade
        return total_grade / len(self.students)



lisa = Student("Alisa", 6)
masha = Student("Maria", 2)
andriiko = Student("Andriy", 50)
volodumer = Student("Volodya", 23)
gleb = Student("Gleb", 100)

class1 = Class(111)
class2 = Class(222)
class3 = Class(333)

teacher_1 = Teacher("Voloddka", "real life", class3)
teacher_2 = Teacher("Nastya", "astophysic", class2)

my_school = School("ItStep", [lisa, masha, andriiko, volodumer, gleb])
print("Початкові студенти")
for student in my_school.students:
    print(student)

my_school.admit_student(Student("Zhenia", 77))
my_school.expel_student(Student("Volodya", 23))
my_school.expel_student(Student("Gleb", 100))
my_school.add_class(class1)
my_school.add_class(class2)
my_school.add_class(class3)

class1.add_student(volodumer)
class2.add_student(lisa)
class3.add_student(gleb)
class3.add_student(masha)

my_school.add_teacher(teacher_1)
my_school.add_teacher(teacher_2)

print("Оновлення")
for student in my_school.students:
    print(student)
for class_obj in my_school.classes:
    print(f"Класи які наявні в школі {class_obj.number}")
for teacher in my_school.teachers:
    print(f"Вчителі які працюють вв школі {teacher.name}")
print(my_school.get_school_statistics())
print(class1.get_average_grade())