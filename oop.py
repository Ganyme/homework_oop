# Создание классов и методов к ним
class Students:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturers) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in self.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_rate(self):
        counter = 0
        sum = 0
        for grade in self.grades.values():
            for mark in grade:
                sum += int(mark)
                counter += 1
        return sum / counter

    def __str__(self):
        res = f'Имя: {self.name} ' \
              f'Фамилия: {self.surname} ' \
              f'Средняя оценка за домашние задания: {self._average_rate()} ' \
              f'Курсы в процессе изучения: {self.courses_in_progress} ' \
              f'Завершенные курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Students):
            print('Incorrect name, he/she is not a student')
            return
        return self._average_rate() < other._average_rate()

class Mentors:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturers (Mentors):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_rate(self):
        counter = 0
        sum = 0
        for grade in self.grades.values():
            for mark in grade:
                sum += int(mark)
                counter += 1
        return sum / counter

    def __str__(self):
        res = f'Имя: {self.name} Фамилия: {self.surname} Средняя оценка за лекции: {self._average_rate()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturers):
            print('Incorrect name, he/she is not a lecturer')
            return
        return self._average_rate() < other._average_rate()

class Reviewers (Mentors):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Students) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} Фамилия: {self.surname}'
        return res

# Создание экземпляров
student1 = Students("Ivan", "Holod", "m")
student1.finished_courses += ["Git"]
student1.courses_in_progress += ['Python']
student1.grades['Git'] = [10, 10, 10]
student1.grades['Python'] = [10, 9, 10]

student2 = Students("Anne", "Mila", "w")
student2.finished_courses += ["Git"]
student2.courses_in_progress += ['Python']
student2.grades['Git'] = [8, 9, 9]
student2.grades['Python'] = [10, 10, 9]

lecturer1 = Lecturers('Oleg', 'Ivanov')
lecturer1.grades['Git'] = [10, 10, 8]
lecturer1.grades['Python'] = [10, 10, 10]

lecturer2 = Lecturers('Katya', 'Kholod')
lecturer2.grades['Python'] = [9, 8, 10]
lecturer2.grades['Git'] = [5, 6, 7]

reviewer1 = Reviewers('Ivan', 'Soloviev')
reviewer1.courses_attached.append('Python')
reviewer1.courses_attached.append('Git')

reviewer2 = Reviewers('Andrey', 'Hot')
reviewer2.courses_attached.append('Python')
reviewer2.courses_attached.append('Git')

# Вызов методов
print(student1)
print(student2)
student1.rate_lecturers(lecturer2, 'Python', 10)
student2.rate_lecturers(lecturer2, 'Python', 8)
print(lecturer2.grades)
print(student1 > student2)

print(lecturer1)
print(lecturer2)
print(lecturer1 > lecturer2)

print(reviewer1)
print(reviewer2)
reviewer1.rate_hw(student1, 'Python', 7)
print(student1.grades)
reviewer2.rate_hw(student2, 'Python', 10)
print(student2.grades)

# Подсчет средней оценки за ДЗ на курсе
def average_course_hwgrade(students_list, course):
    """The function counts average grade on a course"""
    for student in students_list:
        summa = 0
        counter =0
        for grade in student.grades[course]:
            summa += int(grade)
            counter += 1
    return print(f'Средняя оценка на курсе {course} {summa / counter}')


students_list_for_count = [student1, student2]
average_course_hwgrade(students_list_for_count, "Python")
average_course_hwgrade(students_list_for_count, "Git")


# Подсчет средней оценки за лекции по всем лекторам на курсе
def average_course_lecgrade(lecturers_list, course):
    """The function counts average grade on a course"""
    for lecturer in lecturers_list:
        summa = 0
        counter =0
        for grade in lecturer.grades[course]:
            summa += grade
            counter += 1
        print(f'Средняя оценка лектора {lecturer.name} {lecturer.surname} на {course} — {summa / counter}')


lecturers_list_for_count = [lecturer1, lecturer2]
average_course_lecgrade(lecturers_list_for_count, "Python")
average_course_lecgrade(lecturers_list_for_count, "Git")