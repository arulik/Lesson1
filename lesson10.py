from dz_functions_module import *

my_list = ['thomas', 'andrew', 'kris', 'antony']

my_list_int_str = ['thomas', 'andrew', 'kris', 'antony', 20, 10, 5]

my_str = 'abcdefghaabc'

my_str_2 = 'abcde'

my_result = []
for i in my_str:
    for j in my_str_2:
        if i == j:
            my_result.append(i)
print(my_result)
