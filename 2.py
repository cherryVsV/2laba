'''Напишите скрипт, позволяющий искать в заданной директории и в ее
подпапках файлы-дубликаты на основе сравнения контрольных сумм
(MD5). Файлы могут иметь одинаковое содержимое, но отличаться
именами. Скрипт должен вывести группы имен обнаруженных файловдубликатов. '''
import os
import hashlib

def printDirectory():
    try:
        path = input("Введите путь: ")
        return path
    except(OSError,FileNotFoundError):
        print("Ведите путь правильно")
        printDirectory()
path = printDirectory()
filef = os.listdir(path)
print(filef)
def getmd5(filename):
    hashs = hashlib.md5()
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        filer= f.read()
        hashs.update(filer.encode('utf-8'))
    return hashs.hexdigest()
dict = {}
dublicates = {}
for top, dirs, files in os.walk(path):
    for i in files:
        namefile = os.path.join(top, i)
        namefile = str(namefile)
        md5 = getmd5(namefile)
        print(md5, 'utf-8')
        if md5 in dict.keys():
            dublicates[md5] = str(namefile + '-' + dict[md5])
        dict[md5] = namefile
print(dict, '\n')
print('Dublicates: ', dublicates)











