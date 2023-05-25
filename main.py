import logging

class StudentProcessor:
    def __init__(self):
        self.students = []
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())
    def add_student(self, student):
        self.students.append(student)
        self.logger.info(f"{student} був до даний до списку студентів")
    def remove_student(self, student):
        try:
            self.students.remove(student)
            self.logger.info(f"{student} був видалений зі списку студентів")
        except:
            print(f"Студента {student} не було знайде в списку студентів")
    def process_students(self):
        for student in self.students:
            self.logger.info(f"{student} є студентом школи")

name = StudentProcessor()
student_1 = 'Zhenya'
student_2 = 'Zahar'
student_3 = 'Volodbmer'
student_4 = 'Gleb'
name.students = [student_1, student_2, student_3]
name.add_student(student_4)
name.remove_student(student_3)
name.process_students()

