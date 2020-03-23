'''Задан путь к директории с музыкальными файлами (в названии
которых нет номеров, а только названия песен) и текстовый файл,
хранящий полный список песен с номерами и названиями в виде строк
формата «01. Freefall [6:12]». Напишите скрипт, который корректирует
имена файлов в директории на основе текста списка песен.'''
import os
path = os.getcwd() + "\\music"
def GetList(path):
    with open(path, 'r', encoding = 'utf-8') as f:
        return f.readlines() 

def Rename(path):
    for filename in os.listdir(path):
        if filename[-4:] == ".mp3":
            for i in GetList(path+"\\Music.txt"):
                if(filename[:-4])in i and os.path.exists(path+"\\"+filename):
                    os.replace(path+"\\"+filename, path+"\\"+i[:-1]+".mp3")
                    break
Rename(path)
    