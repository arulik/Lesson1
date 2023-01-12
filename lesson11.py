def censore(filename, list):
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


list = ['bob', 'russian', 'putin']
censore("c:/temp/lesson11.txt", list)

