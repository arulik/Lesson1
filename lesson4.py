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


n = 7
for h in range(n):
    for w in range(n*2):
        if n == w:
            print('*')
        else:
            print(' ')
print()