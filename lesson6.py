from random import randint

'''
3. Даны списки my_list_1 и my_list_2. Создать список my_result в который вначале поместить элементы на четных местах из
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

# my_list = [randint(1, 500) for i in range(10)]
# print(my_list)
# len=len(my_list)
# my_list.append(0)
# my_list[len]=my_list[0]
# my_list.pop(0)
# print(my_list)

# my_list = [randint(1, 500) for i in range(10)]
# print(my_list)
# len=len(my_list)
# my_list.append(0)
# my_list[len]=my_list[0]
# my_list.pop(0)
# for i in my_list:
#     my_list.append(my_list.pop(0))
# print(my_list)


'''
*6. Дана строка в которой есть числа (разделяются пробелами). Например "43 больше чем 34, но меньше чем 56".
Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке. Для данного примера ответ - 133.
'''
my_str = '43 больше чем 34, но меньше чем 56'
s = 0
for i in my_str:
    if i.isdigit():
        s+=int(i)
print(s)

'''
*7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit и r_limit, которые точно находятся в
этой строке. Причем l_limit левее чем r_limit. В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими
 символами. my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
'''


'''
*8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список. Если строка
 содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен
 подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_'](используйте срезы длинны 2)
'''


'''
*9. Дан список чисел. Определите, сколько в этом списке элементов, которые больше суммы двух своих соседей
 (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов. Крайние элементы списка никогда не учитываются,
  поскольку у них недостаточно соседей. Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
'''



'''*10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
Например [1, 2, 3, "11", "22", 33] Создать новый список в который поместить только строки из my_list
'''

'''
11. Дана строка my_str. Создать список в который поместить те символы из my_str, которые встречаются
в строке ТОЛЬКО ОДИН раз.
'''

# my_str = str('hello world')
# my_set = set(my_str)
# my_list = (list(my_set))
# my_results = []
# for i in my_list:
#     my_results.append(i)
# print(my_results)


'''
*12. Даны две строки. Создать список в который поместить те символы,которые есть в обеих строках хотя бы раз.
'''
str1="aaaasdf1"
str2="asdfff2"
my_set1= set(str1)
my_set2=set(str2)
print(list(my_set1)+list(my_set2))

'''
*13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках, но в каждой
 ТОЛЬКО ПО ОДНОМУ разу. Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"],
  т.к. эти символы есть в каждой строке по одному разу
'''

str1="aaaasdf1"
str2="asdfff2"
my_set =set(str1+str2)
print(list(my_set))