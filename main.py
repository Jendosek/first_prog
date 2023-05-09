#///classes///dubl_2
#1  симулятор навчального закладу
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students  #список
    def admit_student(self, student):
        self.students.append(student)
        print(f'{}')  #дописати коли створимо клас студентів

class Students