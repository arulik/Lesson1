'''
print('*** Калькулятор ***')
first_num = float(input('Введіть перше число : '))
second_num = float(input('Введіть друге число: '))
operators = input('Що з ними зробити?: ')
if operators == '+':
    print(first_num + second_num)
elif operators == '-':
    print(first_num - second_num)
elif operators == '/':
    if second_num == 0:
        print('На 0 ділити не можна!')
    print(first_num/second_num)
elif operators == '*':
    print(first_num*second_num)
elif operators == '**':
    print(first_num**second_num)
else:
    print('Невідомий оператор')

print('*** Квадрати натуральних чисел ***')
number = int(input('Введіть число: '))
for i in range(1, number):
    if i**2 < number:
        print(i**2, end=' ')


number=float(input('Виберіть число: '))
if number % 2 != 0:
    print('Просте число')
elif number == 2:
    print('Просте число')
else:
    print('Складене число')

'''

mushroom = int(input('Кількість грибів: '))
last_num = int(mushroom) % 10
variable = (' ')
variable2 = ('а')
variable3 = ('ів')
if last_num == 1:
    print(f'Маша нашла в лесу {mushroom} гриб{variable}')
elif last_num in range(2,5):
    print(f'Маша нашла в лесу {mushroom} гриб{variable2}')
else:
    print((f'Маша нашла в лесу {mushroom} гриб{variable3}'))


