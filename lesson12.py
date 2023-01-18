'''
Реализовать программу(несколько функций) цензор.
Принимает файл с текстом и список слов.
На выходе:
1) новый файл с тем же текстом, но заданные слова заменены на звездочки,
2) файл stat.json(формат данных JSON) со статисткой(обновляемый) в виде:
 название файла, список слов, сколько раз каждое слово встретилось в тесте.
3)файл stat.csv(формат данных csv) со статисткой(обновляемый) в виде:
 название файла, список слов, сколько раз каждое слово встретилось в тесте.
'''
import json
import csv


def censore(filename, list):
    '''
    Цензор, цензурує слова із заданого списку та заміняє їх на зірочки
    :param filename:
    :param list:
    :return:
    '''
    with open(filename, "r") as file:
        result = file.read()
    for item in result:
        for i in list:
            censore_line = ''
            for cline in range(len(i)):
                censore_line += '*'
            result = result.replace(i, censore_line)
    with open('c:\\temp\censored.txt', "w") as file:
        file.write(result)


def write_stat_json(filename: str, list):
    '''
     Записує назву файла та кількість слів із списку які були знайдені і замінені в файлі, файл дописується
     а не перезаписує дані.
    :param filename:
    :param list:
    :return:
    '''
    with open(filename, 'r') as file:
        text = file.read()
    result = {}
    text = clear_sym(text)
    new = []
    filedata = {}
    for word in text.split():
        if word in list:
            if word not in result:
                result[word] = 1
            else:
                result[word] += 1

    filedata['censored words'] = result
    filedata['filename'] = filename
    filename = "stat.json"
    with open('stat.json', "r") as file:
        data = json.load(file)
    data.append(filedata)
    with open('stat.json', "w") as file:
        json.dump(data, file)


def write_stat_csv(filename: str, list):
    '''
     Записує назву файла та кількість слів із списку які були знайдені і замінені в файлі, файл дописується
     а не перезаписує дані.
    :param filename:
    :param list:
    :return:
    '''
    with open(filename, 'r') as file:
        text = file.read()
    result = {}
    text = clear_sym(text)
    new = []
    filedata = {}
    for word in text.split():
        if word in list:
            if word not in result:
                result[word] = 1
            else:
                result[word] += 1

    filedata['censored words'] = result
    filedata['filename'] = filename
    filename = "stat.json"
    with open('stat.csv', 'rt') as file:
        reader = csv.DictReader(file, delimiter=';')
    print(reader.)
    # with open('stat.csv', 'a') as file:
    #     writer = csv.DictWriter(file, fieldnames=filedata.keys(), delimiter=';')
    #     writer.writeheader()
    #     writer.writerow(filedata)
    # with open('stat.json', "r") as file:
    #     data = json.load(file)
    # data.append(filedata)
    # with open('stat.json', "w") as file:
    #     json.dump(data, file)


def clear_sym(text):
    '''
    Видаляє лтшні елементи із тексту для зручного читання файлу
    :param text:
    :return:
    '''
    sym = [',', '.', ':', '!']
    for i in sym:
        text = text.replace(i, ' ')
    return text


list = ['bob', 'russian', 'putin', 'test', 'tost']
censore("c:/temp/lesson11.txt", list)
# write_stat("c:/temp/lesson11.txt", list)
write_stat_csv("c:/temp/lesson11.txt", list)
