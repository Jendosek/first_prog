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
        """expelled_student ="""
        pass

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



"""multiply = lambda x, y: x*y
print(multiply(2,5))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_numbers = list(filter(lambda a: a % 2 == 0, numbers))
print(filtered_numbers)"""