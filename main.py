# schoolers = float(input('number of sch:'))
# apples = float(input('num of apple:'))

# print(f'{(apples / schoolers)}',type(apples / schoolers))
'''
a = int(input('a=:'))
b = int(input('b=:'))
x = a / b
print("яблок у кожного школяра: " + str(int(x)))
print("яблок в корзині: " + str((float(x)-int(x))*b))
'''


apple = int(input('Введіть кількість яблок: '))
people = int(input('Введіть кількість школярів: '))
per_people = apple // people
bag = int(apple % people)

print("яблок у кожного школяра: " + str(per_people))
print("яблок в корзині: " + str(bag))






