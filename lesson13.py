'''
1. Создать класс Employee содержащий следуюущие свойства:
    'firstname': 'Ivasik',
    'lastname': 'Telesik',
    'age': 13,
    'e-mail': 'ivasik-telesik1732@izkurnanog.ua',
    'skills': ['ходить', "говорить", "кодить"],
    'people_lang': ['Україньська', "Англійська"],
    'coding_lang': ['Python', "C++", "lisp"],
методы добавить на свое усмотрение(удобство нужно)
добавить метод записи данных сотрудника в файл(JSON/CSV)
*добавить метод создания объекта сотрудника на основании файла
*2. Создать класс Employer содержащий следующие свойства:
    'name': 'Roga i kopita',
    'address':'some address'
    'employees': []
должны присутствовать методы добавления/удаления сотрудников
методы записи/чтения сотрудников в/из файла
'''
import json
import csv


class employee:
    firstname = 'Ivasik'
    lastname = 'Telesik'
    age = 13
    email = 'ivasik_telesik1732@izkurnanog.ua'
    skills = ['ходить', "говорить", "кодить"]
    people_lang = ['Україньська', "Англійська"]
    coding_lang = ['Python', "C++", "lisp"]
    card_emlpoyee = []

    def set_emloyee(self, firstname, lastname, age):
        '''
        Введення початкових данних співробітника
        :param firstname:
        :param lastname:
        :param age:
        :return:
        '''
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def write_card_json_employer(self):
        '''
        Створення файлу json з данними співробітника
        :return:
        '''
        data = {}
        data['firstname'] = self.firstname
        data['lastname'] = self.lastname
        data['age'] = self.age
        data['email'] = self.email
        data['skills'] = self.skills
        data['people_lang'] = self.people_lang
        data['coding_lang'] = self.coding_lang

        with open(f'{self.firstname} {self.lastname}.json', "w", encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False)

    def write_card_csv_employer(self):
        '''
        Створення файлу csv з данними співробітника
        :return:
        '''
        data = {}
        data['firstname'] = self.firstname
        data['lastname'] = self.lastname
        data['age'] = self.age
        data['email'] = self.email
        data['skills'] = self.skills
        data['people_lang'] = self.people_lang
        data['coding_lang'] = self.coding_lang

        with open(f'{self.firstname} {self.lastname}.csv', "w", encoding='utf8') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys(), delimiter=';')
            writer.writeheader()
            writer.writerow(data)

    def create_card_employer(self):
        '''
        Фунуція обёєднує всі властивості співробітника в 1 словник(для зручності)
        :return:
        '''
        data = {}
        data['firstname'] = self.firstname
        data['lastname'] = self.lastname
        data['age'] = self.age
        data['email'] = self.email
        data['skills'] = self.skills
        data['people_lang'] = self.people_lang
        data['coding_lang'] = self.coding_lang
        self.card_eployee = data

    def set_email(self, email):
        '''
        Задати електронну пошту
        :param email:
        :return:
        '''
        self.email = email

    def set_skills(self, skills_list):
        '''
        Задати вміння
        :param skills_list:
        :return:
        '''
        self.skills = skills_list

    def check_skills(self, skill):
        '''
        Перевірка наявності вмінь у співробітника
        :param skill:
        :return:
        '''
        if skill in self.skills:
            return True
        else:
            return False

    def get_list_employee(self):
        '''
        Отримати список співробітників з файлу json
        :return:
        '''
        filename = "list_employee.json"
        with open(filename, "r", encoding='utf8') as file:
            data = json.load(file)
        return data

    def add_employee_to_list(self):
        '''
        Додати співробітника до списку співробітників в файлі json
        :return:
        '''
        data = self.get_list_employee()
        if self.search_employee_by_name_firstname(self.firstname, self.lastname):
            print('Такий співробітник вже є')
        else:
            data.append(self.card_eployee)
            with open("list_employee.json", "w", encoding='utf8') as file:
                json.dump(data, file, ensure_ascii=False)

    def del_employee_to_list(self):
        '''
        Видалити співробітника зі списку співробітників
        :return:
        '''
        new_list = []
        data = self.get_list_employee()
        for emp in range(len(data)):
            if self.firstname != data[emp]['firstname'] and self.lastname != data[emp]['lastname']:
                new_list.append(data[emp])
        with open("list_employee.json", "w", encoding='utf8') as file:
            json.dump(new_list, file, ensure_ascii=False)

    def search_employee_by_name_firstname(self, name, lastname):
        '''
        Знайти співробітника по імені та фамілії в списку співробітників
        :param name:
        :param lastname:
        :return:
        '''
        list_emp = []
        for emp in self.get_list_employee():
            if name == emp['firstname'] and lastname == emp['lastname']:
                list_emp.append(emp)
        return list_emp

    def get_object_from_file(self, filename):
        '''
        Додавання об`єкта з файлу
        :return:
        '''
        with open(filename, "r", encoding='utf8') as file:
            data = json.load(file)
        self.firstname = data['firstname']
        self.lastname = data['lastname']
        self.age = data['age']
        self.email = data['email']
        self.skills = data['skills']
        self.people_lang = data['people_lang']
        self.coding_lang = data['coding_lang']
        return data


new_emp = employee()
# new_emp.set_email('test@test.com.ua')
# new_emp.set_skills(['something', 'something2'])
# new_emp.write_card_json_employer()
# # print(new_emp.check_skills('something'))

# new_emp.add_employee_to_list()
# # print(new_emp.search_employee_by_name_firstname('Ivasik', 'Telesik'))
# for name in new_emp.get_list_employee():
#     print(name)
# new_emp.write_card_csv_employer()
# print(new_emp.get_object_from_file('Ivasik Telesik.json'))


# new_emp.set_emloyee('test', 'test', 21)
# new_emp.create_card_employer()
# new_emp.add_employee_to_list()
new_emp.set_emloyee('tost', 'tost', 22)
# new_emp.create_card_employer()
# new_emp.add_employee_to_list()
new_emp.del_employee_to_list()
print(new_emp.get_list_employee())

# class User:
#     #  (два нижних подчеркивания) перед именем атрибута делают его скрытым за пределами класса(private)
#     __name = str()
#     __age = int()
#     __skills = list()
#
#     def __init(self, name: str, age: int = 18):
#         self.name = name
#         self.age = age
#
#     def __str(self):
#         return f'Name: {self.name}, age: {self.__age}'
    # методы позволяющие работать с private атрибутами называются акцесорами
    # меняющие private атрибут называются сеттерами
    # def set_age(self, age: int):
    #     if age >= 0:
    #         self.__age = age

    # возвращающие private атрибут называются геттерами
    # def get_age(self):
    #     return self.__age
    # Аннотации атрибутов создаются с помощь @property, позволяют получать доступ к private атрибуту через псевдоним
    # при этом технически отрабатывает метод
    # @property
    # def name(self):
    #     return self.__name
    #
    # @property
    # def age(self):
    #     return self.__age

    # аннотация сеттера не может быть описана выше аннотации геттера
    # @age.setter
    # def age(self, age: int):
    #     if age >= 0:
    #         self.__age = age
    #
    # @property
    # def skills(self):
    #     return self.__skills.copy()

#
# obj = User('Anton')
# # print(obj)
# # obj.__age = -12
# # print(obj)
# # print(obj.__age)
# # obj.set_age(-12)
# # obj.age = 234
# print(obj)
# # print(obj.age)
# # print(obj.get_age())
# li = obj.skills
# print(li)
# li.append(123)
# print(li)
# print(obj.skills)

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return f'Name: {self.name}'


class Employee:
    def init(self, name, position):
        self.name = name
        self.__position = position

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    def __str(self):
        return f'Name: {self.name}'


class Employee2(Person):
    def init(self, name, position):
        super().init(name)
        self.position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    def __str(self):
        return f'{super().str()}, Position: {self.__position}'


obj = Employee2('Taras','Contrabas')
print(obj.name)