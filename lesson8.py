# '''
# HW
# 1)Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
#     а) Создать список и поместить туда имя самого молодого человека.
#         Если возраст совпадает - поместить все имена самых молодых.
#     б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
#     в) Посчитать среднее количество лет всех людей из начального списка.
# '''
print('*** Задача 1.а ***')
peoples_list = [
    {"name": "John", "age": 15},
    {"name": "Jack", "age": 45},
    {"name": "Any", "age": 24},
    {"name": "Mary", "age": 16},
    {"name": "Nick", "age": 35},
    {"name": "John2", "age": 15},
]

# min_age = 1110
# for i in peoples_list:
#     if min_age > i['age']:
#         min_age = i['age']
# result_list = []
l = min([i['age'] for i in peoples_list])
result = [i['name'] for i in peoples_list if i['age'] == l]
print(result)
# for i in peoples_list:
#     if min_age == i['age']:
#         result_list.append(i['name'])
# print(result_list)

print('*** Задача 1.б ***')

new_list = []
l_max = max([len(i['name']) for i in peoples_list])

for i in peoples_list:
    if len(i['name']) == l_max:
        new_list.append(i['name'])
print(new_list)

print('*** Задача 1.в ***')
# age = 0
# for i in peoples_list:
#     age += i['age']
# middle_age = age
# print(middle_age / len(peoples_list))
l = sum([i['age'] for i in peoples_list])
print(l / len(peoples_list))

'''
2)Даны два словаря my_dict_1 и my_dict_2.
    а) Создать список из ключей, которые есть в обоих словарях.
    б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
    в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
    г) Объединить эти два словаря в новый словарь по правилу:
        если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
        если ключ есть в двух словарях -
        поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
        {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
'''

my_dict_1 = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
}

my_dict_2 = {
    1: 2,
    2: 1,
    3: 3,
    5: 4,
}
print('*** Задача 2.а ***')
list1 = []
for key in my_dict_1.keys():
    if key in my_dict_2.keys():
        list1.append(key)
print(list1)

print('*** Задача 2.б ***')

list2 = []
for key in my_dict_1.keys():
    if key not in my_dict_2.keys():
        list2.append(key)
print(list2)

print('*** Задача 2.в ***')
new_dict = {}
for key, value in my_dict_1.items():
    if key not in my_dict_2:
        new_dict.update({key: value})
print(new_dict)

print('*** Задача 2.г ***')

new_dict = {}

for key, value in my_dict_1.items():
    new_dict.update({key: value})
for key, value in my_dict_2.items():
    if key in new_dict:
        new_dict.update({key: [my_dict_1[key], value]})
    else:
        new_dict.update({key:value})
print(new_dict)

