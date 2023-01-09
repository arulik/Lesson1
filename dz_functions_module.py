def func_list_reverse(my_list):
    ''' 1) перевертає строку по індексу '''
    my_result = []
    for i in range(0, len(my_list)):
        if i % 2 != 0:
            my_result.append(my_list[i][::-1])
        else:
            my_result.append(my_list[i])
    return my_result


def func_letter_a_first(my_list):
    ''' 2) Повертає елементи в яких перша буква а'''
    letter = 'a'
    my_result = []
    for word in my_list:
        if letter == word[0]:
            my_result.append(word)
    return my_result


def func_if_letter_in(my_list):
    '''3) Якщо є літера 'а' в списку'''
    letter = 'a'
    my_result = []
    for word in my_list:
        if letter in word:
            my_result.append(word)
    return my_result


def func_if_is_str(my_list_int_str):
    '''4) Якщо тип елементу == str вивести цей елемент в новий список'''
    my_result = []
    for word in my_list_int_str:
        if type(word) is str:
            my_result.append(word)
    return my_result


def func_one_letter(my_str):
    '''5) Вивести всі унікальні елементи із строки'''
    my_result = []
    for i in range(len(my_str)):
        if my_str.count(my_str[i]) == 1:
            my_result.append(my_str[i])
    return my_result


def func_one_time_str(my_str, my_str_2):
    '''6) Вивести елементи 2х строк які зустрічаються хоча б один раз'''
    my_result = []
    for i in my_str:
        for j in my_str_2:
            if i == j:
                my_result.append(i)
    return my_result


def func_one_time_str_one_letter(my_str, my_str_2):
    '''7) Вивести символи які є в обох строках але тільки по 1му разу'''
    return func_one_time_str(func_one_letter(my_str), func_one_letter(my_str_2))
