# '''
# HW
# 1)Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
#     а) Создать список и поместить туда имя самого молодого человека.
#         Если возраст совпадает - поместить все имена самых молодых.
#     б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
#     в) Посчитать среднее количество лет всех людей из начального списка.
# '''
# print('*** Задача 1.а ***')
peoples_list = [
    {"name": "John2", "age": 15},
    {"name": "Jack", "age": 45},
    {"name": "Any", "age": 24},
    {"name": "Mary", "age": 16},
    {"name": "Nick", "age": 35},
    {"name": "John2", "age": 15},
]
#
# min_age = 1110
# for i in peoples_list:
#     if min_age > i['age']:
#         min_age = i['age']
# result_list = []
# l = min([i['age'] for i in peoples_list])
# result = [i['name'] for i in peoples_list if i['age'] == l]
# print(result)
# for i in peoples_list:
#     if min_age == i['age']:
#         result_list.append(i['name'])
# print(result_list)

# print('*** Задача 1.в ***')
# age = 0
# for i in peoples_list:
#     age += i['age']
# middle_age = age
# print(middle_age/len(peoples_list))
#
# l = sum([i['age'] for i in peoples_list])
# print(l/len(peoples_list))

print('*** Задача 1.b ***')

result = []
total_result = []
for i in peoples_list:
    result.append(i['name'])
max_l = max(len(i) for i in result)
for i in result:
    if (len(i) == max_l):
        total_result.append(i)
print(total_result)


result = []
max_l =0
total_result = []
for i in peoples_list:
   result.append(i['name'])
   if (len(i['name']) > maxl):
        maxl = len(i['name'])

for ni in result:
    if (len(i) ==max_l):
        total_result.append(i)
print(total_result)