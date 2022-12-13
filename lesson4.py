# print('***Трикутник B ***')
# number = int(input('Введіть висоту трикутника: '))
# user_height = number * 2
# for height in range(0, user_height, 2):
#     for weigth in range(user_height - height):
#         print(end=" ")
#     for weight in range(height + 1):
#         print("*", end=" ")
#     print()
#
# print('\n\n\n*** Генерація чисел***')
# my_string = '0123456789'
# for i in my_string:
#     for j in my_string:
#         print(int(i+j))


print('\n\n*** Трикутник А ***')
user_num=int(input('Введіть висоту трикутника: '))
number = user_num * 2
for height in range(0, number, 2):
    string = ''
    for weight in range((number * 2) * 2):
        if height == number-2:
            if weight == 0:
                string += '  *'
            elif weight <= number-2:
                string += ' *'
        elif number - height == weight or number + height == weight:
            string += '*'
        else:
            string += ' '
    print(string)
