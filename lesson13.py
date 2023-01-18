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


class employee:
    firstname = 'Ivasik'
    lastname = 'Telesik'
    age = 13
    email = 'ivasik_telesik1732@izkurnanog.ua'
    skills = ['ходить', "говорить", "кодить"]
    people_lang = ['Україньська', "Англійська"]
    coding_lang = ['Python', "C++", "lisp"]

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def write_card_json_employer(self):
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

    def set_email(self, email):
        self.email = email

    def skills(self, skills_list):
        self.skills = skills_list

    def check_skills(self, skill):
        if skill in self.skills:
            return True
        else:
            return False


new_emp = employee('Ivan', 'Sidorov', 25)
new_emp.set_email('test@test.com.ua')
new_emp.skills(['something', 'something2'])
new_emp.write_card_json_employer()
print(new_emp.check_skills('something'))
