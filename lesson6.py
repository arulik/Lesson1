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

#
# a = "a14b6fh14"
# chek = []
# for alist in a:
#    if alist in chek:
#        print(alist ," not uniq")
#    else:
#        chek.append(alist)

'''
*4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list стоит на последнем месте.
 Если my_list [1,2,3,4], то new_list [2,3,4,1]
'''

my_list = [6, 7, 7, 1, 2, 3, 4]
print(my_list)
new_list = []
for i in range(1,len(my_list)):
    new_list.append(my_list[i])
new_list.append(my_list[0])
print(new_list)
