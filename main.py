
print('*** Задача про школярів та яблока ***')
apple = int(input('Введіть кількість яблок: '))
people = int(input('Введіть кількість школярів: '))
per_people = apple // people
bag = int(apple % people)
print("яблок у кожного школяра: " + str(per_people))
print("яблок в корзині: " + str(bag))


print('*** Задача про парти для учнів ***')
num_of_class = 3
first_class=int(input('Кількість дітей у першому класі: '))
second_class=int(input('Кількість дітей у другому класі: '))
third_class=int(input('Кількість дітей у третьому класі: '))
main_part = int((first_class + second_class + third_class) // 2)
secondary_part = int(first_class + second_class + third_class) % 2
print(f'Кількість парт для покупки {main_part+secondary_part}')











