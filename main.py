#///classes///dubl_2
#1  симулятор навчального закладу
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students  #список
    def admit_student(self, student):
        self.students.append(student)
        print(f'{student.name} був допущений до школи {self.name}')

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
