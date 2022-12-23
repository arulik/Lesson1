from random import randint

# my_set = set([1,3,5,7,9,9])
# print(my_set)
'''
Даны списки my_list_1 и my_list_2. Создать список my_result в который вначале поместить элементы на четных местах из
my_list_1, а потом все элементы на нечетных местах из my_list_2.
'''
# my_list = [randint(1, 500) for i in range(10)]
# my_list2 = [randint(1, 500) for i in range(10)]
# my_results = []
# print(my_list)
# print(my_list2)
# for i in range(0, len(my_list + 1)):
#     my_results.append(my_list[i])
#     my_results.append(my_list2[i])
# print(my_results)

# my_str = str('hello world')
# my_set = set(my_str)
# my_list = (list(my_set))
# my_results = []
# for i in my_list:
#     my_results.append(i)
# print(my_results)


'''
*4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list стоит на последнем месте.
 Если my_list [1,2,3,4], то new_list [2,3,4,1]
'''

# my_list = [6, 7, 7, 1, 2, 3, 4]
# print(my_list)
# new_list = []
# for i in range(1,len(my_list)):
#     new_list.append(my_list[i])
# new_list.append(my_list[0])
# print(new_list)
'''
*5. Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.[1,2,3,4] -> [2,3,4,1].
Пересоздавать список нельзя! (используйте метод pop)
'''

my_list = [randint(1, 500) for i in range(10)]
print(my_list)
len=len(my_list)
my_list.append(0)
my_list[len]=my_list[0]
my_list.pop(0)
print(my_list)

*6. Дана строка в которой есть числа (разделяются пробелами). Например "43 больше чем 34, но меньше чем 56".
Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке. Для данного примера ответ - 133.
