'''Напишите скрипт, который позволяет ввести с клавиатуры имя
текстового файла, найти в нем с помощью регулярных выражений все
подстроки определенного вида, в соответствии с вариантом. Например,
для варианта № 1 скрипт должен вывести на экран следующее:
Строка 3, позиция 10 : найдено '11-05-2014'
Строка 12, позиция 2 : найдено '23-11-2014'
Строка 12, позиция 17 : найдено '23-11-2014' 
Вариант 8: найдите все логические выражения – подстроки вида
«x&&y», «x&y», где х и у – любые слова. Количество пробелов может
быть также любым'''
import re
def searching(text):
    for i in range(len(text)):
        pattern = re.compile(r'\D+&{1}\D+|\D+&{2}\D+') 
        result = pattern.findall(text[i])
        searchres = pattern.search(text[i])
        if searchres != None:
            print('Строка № ', i, 'Позиция: ', searchres.span(), ' : ', result  )
        else:
            print("В строке № ", i, " cовпадений не найдено")
def FileWork(path):
    filef = open(path)
    filestr = filef.readlines()
    newlines = list(map(lambda x:x.rstrip(), filestr))
    searching(newlines)
def OpenFile():
    try:
        f = input('Bведите путь к файлу \n')
        FileWork(f)
    except(FileNotFoundError, OSError):
        print("Введите путь правильно")
        OpenFile()
OpenFile()


