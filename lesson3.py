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

print('\n*** Квадрати натуральних чисел ***')
number = int(input('Введіть число: '))
for i in range(1, number):
    if i**2 < number:
        print(i**2, end=' ')


number = int(input('Введіть Ваше число: '))
for i in range(2, number // 2 + 1):
    if number % i == 0:
        print('Складене число')
        break
else:
    print('Просте число')


print('\n*** Задача про гриби ***')
mushroom = int(input('Кількість грибів: '))
last_num = int(mushroom) % 10
exception = int(mushroom) % 100
variable_pass = (' ')
variable_range = ('а')
variable_else = ('ів')
if last_num < 10 and exception == 11 or exception in range(12,15):
    print((f'Маша знайшла у лісі {mushroom} гриб{variable_else}'))
elif last_num == 1:
    print(f'Маша знайшла у лісі {mushroom} гриб{variable_pass}')
elif last_num in range(2, 5):
    print(f'Маша знайшла у лісі {mushroom} гриб{variable_range}')
else:
    print((f'Маша знайшла у лісі {mushroom} гриб{variable_else}'))
