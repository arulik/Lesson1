'''
1. Инициализация класса с одним параметром - имя директории.
2. Написать метод класса, который создает атрибут класса в ввиде словаря
{'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
Подпапки учитывать только первого уровня вложения. Папка в папке в папке - такое не брать ))
{'filenames': [файл1, файл2, файл7], 'dirnames': [папка1, папка2]}
2. Написать метод класса, которая получает булевое значение (True/False).
Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.
3. Написать метод класса, которая получает строку, которая может быть
или именем файла, или именем папки. (В имени файла должна быть точка).
В зависимости от того, что функция получила (имя файла или имя папки) - записать его
в соответствующий список и вернуть обновленный словарь.
4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
Написать метод класса, которая получает имя директори и словарь по примеру из задания 1.
Функция проверяет соответствие полученного словаря и реальной файловой системы в полученной папке и,
если надо, создает нужные папки и пустые файлы, в соответствии со структурой словаря.
Пример:
создали на основании данных в папке -> {'filenames': [файл1, файл2, файл7], 'dirnames': [папка1, папка2]}
передали в метод -> {'filenames': [файл1, файл7, файл13], 'dirnames': [папка11, папка2]}
в результате необходимо создать файл13 и папка11
'''

import os


class directory:
    dirname = ''
    dict = {}

    def __init__(self, dirname: str = 'dir'):
        """
        присвоєння об`єкта = за замовчуванням це папка dir
        :param dirname:
        """
        self.dirname = dirname

    def __str__(self):
        '''
        Вивід результату
        :return:
        '''
        return f'{self.dict}'

    def create_dict_list(self):
        '''
        Сворення словника з спиками файлів та папок в директорії
        :param dir:
        :return:
        '''
        dir_path = self.dirname
        files = []
        dirs = []
        for (dir_path, dir_names, file_names) in os.walk(dir_path):
            files.extend(file_names)
            dirs.extend(dir_names)
        self.dict['filenames'] = files
        self.dict['dirnames'] = dirs
        return self.dict

    def sort(self, type_sort=True):
        '''
        Функція сортування, True - сортування за алфавітом, False - реверс, вивід новий словник з
        відсортованними данними
        :param type_sort:
        :return:
        '''
        new_dict = {}
        if type_sort:
            new_dict['filenames'] = sorted(self.dict['filenames'], reverse=False)
            new_dict['dirnames'] = sorted(self.dict['dirnames'], reverse=False)
            return new_dict
        else:
            new_dict['filenames'] = sorted(self.dict['filenames'], reverse=True)
            new_dict['dirnames'] = sorted(self.dict['dirnames'], reverse=True)
            return new_dict

    def check_if_dir_or_file(self, string: str):
        '''
        Додавання файлів/папок в словник
        :param string:
        :return:
        '''
        if '.' in string:
            self.dict['filenames'].append(string)
            return self.dict
        else:
            self.dict['dirnames'].append(string)
            return self.dict


new_dir = directory()
new_dir.create_dict_list()
# print(new_dir.check_if_dir_or_file('m'))
print(new_dir)
# # print(new_dir.sort(False))
# print(new_dir.sort(True))
# print(new_dir)

