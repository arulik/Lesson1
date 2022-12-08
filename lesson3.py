'''
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
'''

number = int(input('Input number: '))

#for number in range(start_number,number):
#    print(number**2, end=' ')

for i in range(1, number):
    if i**2 < number:
        print(i**2, end=' ')
