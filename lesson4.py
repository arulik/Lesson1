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

# if w % 2 == 0:
#     str1 += ('  ')
# else:
#     str1 += ('*')


n = 7 * 2
for h in range(0, n, 2):
    str1 = ''
    for w in range((n * 2) * 2):
        if h == n-2:
            print(' ')
        elif n - h == w or n + h == w:
            str1 += ('*')
        else:
            str1 += (' ')
    print(str1)
