from typing import AsyncGenerator


class Student:
    def __init__(self, name, age, grade) -> None:
        self.name = name
        self.age = age
        self.grade = grade  #0-100
        #pass
    
    def getGrade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students) -> None:
        self.name = name
        self.max_students = max_students
        self.students = []
        #pass
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.getGrade()
        return value/ len(self.students)

student1 = Student(name="Tim", age=19, grade=90)
student2 = Student(name="Bill", age=18, grade=95)
student3 = Student(name="Joe", age=20, grade=85)

course1 = Course(name="Science", max_students=2)
print(course1.add_student(student1))
print(course1.add_student(student2))
print(course1.add_student(student2))
print(course1.get_average_grade())
