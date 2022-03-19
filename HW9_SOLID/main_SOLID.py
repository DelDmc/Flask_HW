import datetime

from faker import Faker


class DateConverter:
    @staticmethod
    def convert(date_of_birth):
        date = str(date_of_birth)
        d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        return d.strftime('%d.%m.%Y')


class PersonGenerator:
    @staticmethod
    def generate_person(count, age_start_date, age_end_date):
        faker = Faker()
        persons_list = []
        for _ in range(count):
            date_of_birth = faker.date_time_between(start_date=f"-{age_start_date}y", end_date=f"-{age_end_date}y")
            date_converted = DateConverter.convert(date_of_birth)
            person = {
                'first_name': str(faker.first_name()),
                'last_name': str(faker.last_name()),
                'date_of_birth': date_converted,
                'age': Person.age(date_converted)
            }
            persons_list.append(person)
        return persons_list


class Person:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.persons = []

    @classmethod
    def convert_date_of_birth(cls, date_of_birth):
        return datetime.datetime.strptime(date_of_birth, '%d.%m.%Y')

    @classmethod
    def age(cls, date_of_birth):
        return datetime.datetime.now().year - cls.convert_date_of_birth(date_of_birth).year


class Student(Person):
    def __init__(self, first_name, last_name, date_of_birth, **kwargs):
        super().__init__(first_name, last_name, date_of_birth)
        self.grade = kwargs.get("grade", '')

    def student_info(self):
        return f'{self.first_name} '\
               f'{self.last_name} '\
               f' Grade: {self.grade}'\
               f' Age: {self.age(self.date_of_birth)}'


class Employee(Person):
    def __init__(self, first_name, last_name, date_of_birth, **kwargs):
        super().__init__(first_name, last_name, date_of_birth)
        self.salary = kwargs.get("salary", '')
        self.years_of_experience = kwargs.get("experience", '')


class Faculty(Employee):
    pass


class Assistant(Faculty):
    pass


class Professor(Faculty):
    def __init__(self, first_name, last_name, date_of_birth, **kwargs):
        super().__init__(first_name, last_name, date_of_birth, **kwargs)
        self.jobtitle = 'Professor'

    def professor_info(self):
        return f'{p1.jobtitle} ' \
               f'{self.first_name} '\
               f'{self.last_name} '\
               f' Age: {self.age(self.date_of_birth)}'\
               f' Experience: {self.years_of_experience}'


class Group:
    def __init__(self, name):
        self.name = name
        self._students = []
        self._professors = []

    def add_student(self, *args):
        self._students.append(args)

    def add_professor(self, *args):
        self._professors.append(*args)

    def count_students(self):
        return len(self._students)

    def __str__(self):
        return f'\nGroup {self.name} ' \
               f'\nQty of students: {self.count_students()} ' \
               f'\nStudents:{self._students} ' \
               f'\nProfessors:{self._professors}'


s1 = Student(
    'Ashley',
    'Collins',
    '26.12.2000',
    grade=1
)
s2 = Student(
    'Bradley',
    'Smitt',
    '17.06.2001',
    grade=1
)
s3 = Student(
    'James',
    'Blake',
    '04.09.2000',
    grade='1'
)
p1 = Professor(
    'John',
    'Doe',
    '05.01.1945',
    experience='45',
    salary='4500'
)

g1_a = Group('A')
g1_a.add_student(s1.student_info())
g1_a.add_student(s2.student_info())
g1_a.add_student(s3.student_info())

g1_a.add_professor(p1.professor_info())

print(g1_a.__str__())
persons_list = PersonGenerator.generate_person(15, 25, 18)

for i in persons_list:
    if i['age'] < 22:
        i['grade'] = 1
        student_info = f"{i['first_name']} " \
                       f" {i['last_name']} " \
                       f" Grade: {i['grade']} " \
                       f"Age: {i['age']}"
        g1_a.add_student(student_info)
print(g1_a.__str__())



