from dz_functions_module import func_list_reverse
my_list = ['Thomas', 'Andrew', 'Kris', 'Antony']



letter = 'a'
my_result = []
for word in my_list:
    if letter in word:
        my_result.append(word)
print(my_result)