class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    grades = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

awesome_reviewer = Reviewer('Awesome', 'Mate')
awesome_reviewer.courses_attached += ['Python']

the_best_lecturer = Lecturer('Best', 'Lecturer')
the_best_lecturer.courses_attached += ['Python']

awesome_reviewer.rate_hw(best_student, 'Python', 5)
awesome_reviewer.rate_hw(best_student, 'Python', 2)
awesome_reviewer.rate_hw(best_student, 'Python', 6)

best_student.rate_lecturer(the_best_lecturer, 'Python', 3)
best_student.rate_lecturer(the_best_lecturer, 'Python', 6)
best_student.rate_lecturer(the_best_lecturer, 'Python', 7)

print(best_student.grades)
print(the_best_lecturer.grades)