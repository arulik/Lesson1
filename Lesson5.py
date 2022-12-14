from random import randint

my_list = [randint(1, 500) for i in range(300)]
for i in my_list:
    if i >= 100:
        print(i, end='\t')


my_list = [randint(1, 500) for i in range(300)]
my_results = []
for i in my_list:
    if i >= 100:
        my_results.append(i)
print(my_results)

my_list = [randint(1, 5) for i in range(3)]
if len(my_list) <= 2:
    my_list.append(0)
elif len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)

