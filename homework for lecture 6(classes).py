class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        grade_ = sum(self.grades.volues()) / len(self.grades.volues())
        return grade_

    def __str__(self):
        info = f'Имя: {self.name}/n ' \
               f'Фамилия: {self.surname}/n ' \
               f'Средняя оценка за лекции: {self.average_grade()}/n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}/n ' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return info

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет такого студента!')
            return
        if isinstance(other, Student):
            self.average_grade < other.average_grade
            print(f'{self.name} учится лучше, чем {other.name}')
        elif self.average_grade > other.average_grade:
            print(f'{self.name} учится хуже, чем {other.name}')
        else:
            self.average_grade == other.average_grade
            print(f'у студентов {self.name} и {other.name} одинаковая успеваемость')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades = {}

    def average_grade(self):
        grade_ = sum(self.grades.volues()) / len(self.grades.volues())
        return grade_

    def __str__(self):
        info = f'Имя: {self.name}/n Фамилия: {self.surname}/n Средняя оценка за лекции: {self.average_grade()}'
        return info

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет такого лектора!')
            return
        if isinstance(other, Lecturer):
            self.average_grade < other.average_grade
            print(f'{self.name} преподает лучше, чем {other.name}')
        elif self.average_grade > other.average_grade:
            print(f'{self.name} преподает хуже, чем {other.name}')
        else:
            self.average_grade == other.average_grade
            print(f'лекторы {self.name} и {other.name} оба красавчики')


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
        info = f'Имя: {self.name}/n Фамилия: {self.surname}'
        return info


#
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)
# print(best_student.courses_in_progress)
# print(best_student.grades)
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
# print(cool_mentor.courses_attached)

student1 = Student('Thom', 'Hardy', 'man')
student2 = Student('Christian', 'Bale', 'man')

mentor1 = Mentor('Anne', 'Hathaway')
mentor2 = Mentor('Heath', 'Ledger')

lecturer1 = Lecturer('Marion', 'Cotillard')
lecturer2 = Lecturer('Gary', 'Oldman')

reviewer1 = Reviewer('Katie', 'Holmes')
reviewer2 = Reviewer('Liam', 'Neeson')

student_list = [student1, student2]
lecturer_list = [lecturer1, lecturer2]


def student_all_average_grade(students, cours):
    time_list = []
    for student in student_list:
        time_list.append(student.grades.values())
        
