'''Введите с клавиатуры текст. Программно найдите в нем и выведите
отдельно все слова, которые начинаются с большого латинского
символа (от A до Z) и заканчиваются 2 или 4 цифрами, например
«Petr93», «Johnny70», «Service2002». Используйте регулярные
выражения.'''
import re
def search(Vvod):
    text = ''
    splitText = Vvod.split(' ')
    for i in range(len(splitText)):
        pattern = re.compile(r'[A-Z]{1}[a-z]+\d{4}|[A-Z]{1}[a-z]+\d{2}')
        text = pattern.findall(splitText[i])
        if text!=None:
            print(text)
        else:
            print("Совпадений не найдено")
lines = input("Введите текст:\n")
search(lines)