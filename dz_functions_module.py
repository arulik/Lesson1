def func_list_reverse(my_list):
    ''' перевертає строку по індексу '''
    my_result = []
    for i in range(0, len(my_list)):
        if i % 2 != 0:
            my_result.append(my_list[i][::-1])
        else:
            my_result.append(my_list[i])
    return my_result


def func_letter_a_first(my_list):
    ''' Повертає елементи в яких перша буква а'''
    letter = 'a'
    my_result = []
    for word in my_list:
        if letter in word:
            print(word)




