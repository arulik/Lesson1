
print('*** Задача про школярів та яблока ***')
apple = int(input('Введіть кількість яблок: '))
people = int(input('Введіть кількість школярів: '))
per_people = apple // people
bag = int(apple % people)
print("яблок у кожного школяра: " + str(per_people))
print("яблок в корзині: " + str(bag), end='\n\n')


print('*** Задача про парти для учнів ***')
first_class=int(input('Кількість дітей у першому класі: '))
second_class=int(input('Кількість дітей у другому класі: '))
third_class=int(input('Кількість дітей у третьому класі: '))
main_part = int((first_class + second_class + third_class) // 2)
secondary_part = int(first_class + second_class + third_class) % 2
print(f'Кількість парт для покупки {main_part+secondary_part}', end='\n\n')


first_num = int(input("Введіть число для інверсії: "))
second_num = 0
while first_num > 0:
    last_num = first_num % 10
    first_num = first_num // 10
    second_num = second_num * 10 + last_num
print('Число після інверсії:', second_num, end='\n\n')


print('*** Задача для обчислення секунд ***')
sec = int(input('Введіть кількість секунд= '))
sec_value = sec % (24 * 3600)
hour_value = sec_value // 3600
sec_value %= 3600
min_value = sec_value // 60
sec_value %= 60
print(f'{hour_value}:{min_value}:{sec_value}')


