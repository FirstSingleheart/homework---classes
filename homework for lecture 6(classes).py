students_list = []
lecturers_list = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        overall_grade = 0
        grades_count = 0
        if len(self.grades) == 0:
            return 0
        else:
            for grades in self.grades.values():
                if len(grades) > 0:
                    for grade in grades:
                        overall_grade += grade
                        grades_count += 1
            return overall_grade / grades_count

    def __str__(self):
        info = f'Имя: {self.name}\n ' \
               f'Фамилия: {self.surname}\n ' \
               f'Средняя оценка за лекции: {round(self.avg_grade(), 2)}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return info

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет такого студента!')
            return
        if isinstance(other, Student):
            if self.avg_grade() < other.avg_grade():
                return f'{self.name} учится лучше, чем {other.name}'
            elif self.avg_grade() > other.avg_grade():
                return f'{self.name} учится хуже, чем {other.name}'
            else:
                return f'у студентов {self.name} и {other.name} одинаковая успеваемость'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lecturers_list.append(self)

    def avg_grade(self):
        overall_grade = 0
        grades_count = 0
        if len(self.grades) == 0:
            return 0
        else:
            for grades in self.grades.values():
                if len(grades) > 0:
                    for grade in grades:
                        overall_grade += grade
                        grades_count += 1
            return overall_grade / grades_count

    def __str__(self):
        info = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {round(self.avg_grade(), 2)}'
        return info

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет такого лектора!')
            return
        if isinstance(other, Lecturer):
            if self.avg_grade() < other.avg_grade():
                return f'{self.name} преподает лучше, чем {other.name}'
            elif self.avg_grade() > other.avg_grade():
                return f'{self.name} преподает хуже, чем {other.name}'
            else:
                return f'Лекторы {self.name} и {other.name} оба красавчики!'


class Reviewer(Mentor):

    def rate_students(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        info = f'Имя: {self.name}\n Фамилия: {self.surname}'
        return info


def avg_grade_all_students(students_list, course_name):
    all_students_avg_grade = 0
    students_count = 0
    for student in students_list:
        if isinstance(student, Student) and course_name in student.courses_in_progress:
            all_students_avg_grade += student.grades[course_name]
            students_count += 1
    if students_count == 0:
        return 'Ошибка'
    return round(all_students_avg_grade / students_count, 2)


def avg_grade_all_lecturers(lecturers_list, course_name):
    all_lecturers_avg_grade = 0
    lecturers_count = 0
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course_name in lecturer.courses_attached:
            all_lecturers_avg_grade += lecturer.grades[course_name]
            lecturers_count += 1
    if lecturers_count == 0:
        return 'Ошибка'
    return round(all_lecturers_avg_grade / lecturers_count, 2)


mentor1 = Mentor('Anne', 'Hathaway')
mentor2 = Mentor('Heath', 'Ledger')

student1 = Student('Thom', 'Hardy', 'man')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Java']
student1.add_courses('C++')

student2 = Student('Christian', 'Bale', 'man')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Java']
student2.add_courses('C++')

lecturer1 = Lecturer('Marion', 'Cotillard')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Gary', 'Oldman')
lecturer2.courses_attached += ['Python']

reviewer1 = Reviewer('Katie', 'Holmes')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Java']

reviewer1.rate_students(student1, 'Python', 5)
reviewer1.rate_students(student1, 'Python', 5)
reviewer1.rate_students(student1, 'Python', 5)
reviewer1.rate_students(student1, 'Java', 4)
reviewer1.rate_students(student1, 'Java', 5)
reviewer1.rate_students(student1, 'Java', 4)

reviewer2 = Reviewer('Liam', 'Neeson')
reviewer2.courses_attached += ['Python']
reviewer2.courses_attached += ['Java']

reviewer2.rate_students(student2, 'Java', 5)
reviewer2.rate_students(student2, 'Java', 5)
reviewer2.rate_students(student2, 'Java', 5)
reviewer2.rate_students(student2, 'Python', 4)
reviewer2.rate_students(student2, 'Python', 5)
reviewer2.rate_students(student2, 'Python', 3)

student1.rate_lecturer(lecturer1, "Python", 5)
student1.rate_lecturer(lecturer1, "Python", 5)
student1.rate_lecturer(lecturer1, "Python", 5)

student2.rate_lecturer(lecturer2, "Python", 4)
student2.rate_lecturer(lecturer2, "Python", 3)
student2.rate_lecturer(lecturer2, "Python", 4)

print(f'{lecturer1}\n')
print(f'{lecturer2}\n\n')
print(f'{reviewer1}\n')
print(f'{reviewer2}\n\n')
print(f'{student1}\n')
print(f'{student2}\n\n')

print(student1 > student2)
print(lecturer1 > lecturer2)

print(avg_grade_all_students(students_list, 'Python'))
print(avg_grade_all_lecturers(lecturers_list, 'Python'))


