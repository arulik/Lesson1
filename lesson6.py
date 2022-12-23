from random import randint

# my_set = set([1,3,5,7,9,9])
# print(my_set)
'''
Даны списки my_list_1 и my_list_2. Создать список my_result в который вначале поместить элементы на четных местах из
my_list_1, а потом все элементы на нечетных местах из my_list_2.
'''
my_list = [randint(1, 500) for i in range(10)]
my_list2 = [randint(1, 500) for i in range(10)]
my_results= []
print(my_list)
print(my_list2)
for i in my_list:
    my_results.append(i)
for j in my_list2:
    my_results.append(j)
print(my_results)





my_str = str('hello world')
my_set = set(my_str)
my_list = (list(my_set))
my_results = []
for i in my_list:
    my_results.append(i)
print(my_results)

#
# a = "a14b6fh14"
# chek = []
# for alist in a:
#    if alist in chek:
#        print(alist ," not uniq")
#    else:
#        chek.append(alist)
