class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finish_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lector_b, course, grade):
        if isinstance(lector_b, Lector) and course in self.finish_courses and course in lector_b.course_attached:
            if course in lector_b.grades:
                lector_b.grades[course] += grade
            else:
                lector_b.grades[course] = grade
        else:
            print('ошибка')

    def __str__(self):
        self.average_grade = sum(self.grades.values()) / len(self.grades)
        student_card = f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade}\nКурсы в процессе изучения: {", ".join(map(str, self.courses_in_progress))}\nЗавершенные курсы: {", ".join(map(str, self.finish_courses))}'
        return student_card

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение не со студентом !!!')
            return
        return self.average_grade < other.average_grade


class Mentor:
    def __init__(self, name, surname):
        self.course_attached = []
        self.name = name
        self.surname = surname


class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        self.average_grade = sum(self.grades.values()) / len(self.grades)
        lector_card = f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade}'
        return lector_card

    def __lt__(self, other):
        if not isinstance(other, Lector):
            print('Сравнение не с лектором !!!')
            return
        return self.average_grade < other.average_grade


class Reviewer(Mentor):
    def rate_hw(self, student_a, course, grade):
        if isinstance(student_a,
                      Student) and course in student_a.courses_in_progress and course in self.course_attached:
            if course in student_a.grades:
                student_a.grades[course] += grade
            else:
                student_a.grades[course] = grade
        else:
            print('ошибка')

    def __str__(self):
        reviewer_card = f'\nИмя: {self.name}\nФамилия: {self.surname}'
        return reviewer_card


some_stud = Student('Сергей', 'Иванов', 'male')
some_stud.courses_in_progress = ['Python', 'GIT']
some_stud.finish_courses = ['Введение в программирование', 'JS']

another_stud = Student('Александр', 'Петров', 'male')
another_stud.courses_in_progress = ['Python', 'GIT']
another_stud.finish_courses = ['Введение в программирование', 'JS']

teacher1 = Reviewer('Егор', 'Оценкин')
teacher1.course_attached += ['Python', 'GIT']

teacher1.rate_hw(some_stud, 'Python', 10)
teacher1.rate_hw(some_stud, 'GIT', 9)
teacher1.rate_hw(another_stud, 'Python', 8)
teacher1.rate_hw(another_stud, 'GIT', 10)

print(f'{some_stud.name} {some_stud.surname} получил {some_stud.grades}')
print(f'{another_stud.name} {another_stud.surname} получил {another_stud.grades}')

first_lector = Lector('Дмитрий', 'Дмитриев')
first_lector.course_attached += ['JS', 'Python', 'Введение в программирование']
some_stud.rate_lect(first_lector, 'JS', 7)
some_stud.rate_lect(first_lector, 'Введение в программирование', 9)

second_lector = Lector('Алексей', 'Алексеев')
second_lector.course_attached += ['JS', 'Python', 'Введение в программирование']
some_stud.rate_lect(second_lector, 'JS', 10)
some_stud.rate_lect(second_lector, 'Введение в программирование', 7)

print(f'{first_lector.name} {first_lector.surname} получил: {first_lector.grades}')

print(teacher1)

print(first_lector)
print(second_lector)
print()
print(first_lector < second_lector)
print(some_stud)
print(another_stud)
print()
print(some_stud > another_stud)
print()


def avg_hw_grade(stud_list, course):
    grade_sum = 0
    stud_sum = 0
    for i in stud_list:
        grade_sum += i.grades[course]
        stud_sum += 1
    print(f'Средняя оценка за курс {course} составила: {grade_sum / stud_sum}')


stud_list = [some_stud, another_stud]
avg_hw_grade(stud_list, 'Python')


def avg_lect_grade(lector_list, course):
    grade_sum = 0
    lector_sum = 0
    for i in lector_list:
        grade_sum += i.grades[course]
        lector_sum += 1
    print(f'Средняя оценка за лекции по курсу {course} составила: {grade_sum / lector_sum}')


lector_list = [first_lector, second_lector]
avg_lect_grade(lector_list, 'Введение в программирование')
