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
 
some_mentor = Mentor('Ron', 'Dense')
some_mentor.courses_attached += ['Python']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

some_lecturer = Lecturer('John', 'Mate')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

some_reviewer.rate_hw(some_student, 'Python', 5)
some_reviewer.rate_hw(some_student, 'Python', 2)
some_reviewer.rate_hw(some_student, 'Python', 6)

some_student.rate_lecturer(some_lecturer, 'Python', 3)
some_student.rate_lecturer(some_lecturer, 'Python', 6)
some_student.rate_lecturer(some_lecturer, 'Python', 7)

print(some_reviewer)
print(some_lecturer)
print(some_student)