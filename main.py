'''
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


print('*** Інверсія числа ***')
default_num = input("Введіть ціле число: ")
inverse_num = default_num[::-1]
print('Результат:', inverse_num)
'''

#sec = int(input('кількість секунд: '))
#y = int(sec // 60 // 60)
#print(y)
secsec=int(input('sec= '))
sec_value = secsec % (24 * 3600)

