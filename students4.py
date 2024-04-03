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
        
    def _get_average_grade(self, grades):
        grades = self.grades
        result = 0
        ammount = 0
        for i in grades.values():
            for j in i:
                ammount += 1
                result += j
        average = result / ammount
        average = float('{:.1f}'.format(average))
        return average
    
    def __str__(self):
        avg_grade = f'Средняя оценка за домашние задания: {self._get_average_grade(self.grades)}'
        current_courses = f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}'
        finished_courses = f'Завершенные курсы: {", ".join(self.finished_courses)}'
        result = f'Имя: {self.name}\nФамилия: {self.surname}\n{avg_grade}\n{current_courses}\n{finished_courses}'
        return result
    
    def __lt__(self, other):
        return self._get_average_grade(self.grades) < other._get_average_grade(self.grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _get_average_grade(self, grades):
        grades = self.grades
        result = 0
        ammount = 0
        for i in grades.values():
            for j in i:
                ammount += 1
                result += j
        average = result / ammount
        average = float('{:.1f}'.format(average))
        return average
    
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка за лекции: {self._get_average_grade(self.grades)}'
        return result
    
    def __lt__(self, other):
        return self._get_average_grade(self.grades) < other._get_average_grade(self.grades)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result  
        
some_student = Student('Ruoy', 'Eman', 'male')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']
another_student = Student('Luna', 'Lovegood', 'female')
another_student.courses_in_progress += ['Python']
another_student.courses_in_progress += ['Git']
another_student.finished_courses += ['Основы JavaScript']

some_mentor = Mentor('Ron', 'Dense')
some_mentor.courses_attached += ['Python']
another_mentor = Mentor('Phil', 'Yuikes')
another_mentor.courses_attached += ['Python']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']
another_reviewer = Reviewer('Some', 'Buddy')
another_reviewer.courses_attached += ['Python']
another_reviewer.courses_attached += ['Git']

some_lecturer = Lecturer('John', 'Mate')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']
another_lecturer = Lecturer('Will', 'Smith')
another_lecturer.courses_attached += ['Python']
another_lecturer.courses_attached += ['Git']

some_reviewer.rate_hw(some_student, 'Python', 4)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 7)
some_reviewer.rate_hw(some_student, 'Git', 9)

another_reviewer.rate_hw(another_student, 'Python', 7)
another_reviewer.rate_hw(another_student, 'Git', 9)
another_reviewer.rate_hw(another_student, 'Git', 5)
another_reviewer.rate_hw(another_student, 'Python', 8)

some_student.rate_lecturer(some_lecturer, 'Python', 5)
some_student.rate_lecturer(some_lecturer, 'Git', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 8)

another_student.rate_lecturer(another_lecturer, 'Python', 9)
another_student.rate_lecturer(another_lecturer, 'Git', 7)
another_student.rate_lecturer(another_lecturer, 'Python', 8)


def all_students_grades(students, course):
    all_grades = []
    for student in students:
        result = 0
        all_grades.extend(student.grades[course])
        for i in all_grades:
            result += i
    print(result / len(all_grades))

def all_lecturers_grades(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        result = 0
        all_grades.extend(lecturer.grades[course])
        for i in all_grades:
            result += i
    print(result / len(all_grades))

print(some_reviewer)
print()
print(some_lecturer)
print()
print(some_student)
print()
print(another_reviewer)
print()
print(another_lecturer)
print()
print(another_student)
print()
print(some_student < another_student)
print(some_lecturer > another_lecturer)
print()
students = [some_student, another_student]
all_students_grades(students, 'Python')
lecturers = [some_lecturer, another_lecturer]
all_lecturers_grades(lecturers, 'Git')
