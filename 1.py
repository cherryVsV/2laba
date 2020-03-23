'''Напишите скрипт, который читает текстовый файл и выводит символы
в порядке убывания частоты встречаемости в тексте. Регистр символа
не имеет значения. Программа должна учитывать только буквенные
символы (символы пунктуации, цифры и служебные символы слудет
игнорировать). Проверьте работу скрипта на нескольких файлах с
текстом на английском и русском языках, сравните результаты с
таблицами, приведенными в wikipedia.org/wiki/Letter_frequencies'''
try:
    with open(r'1.txt', 'rt', encoding = 'utf-8') as f:
        text = f.readlines()
        newtext = str([x.rstrip() for x in text]).lower()
    print('Read from file:', newtext)
except IOError as err:
    print(err)
    text = []
arr = []
for i in range(len(newtext)):
    if newtext[i].isalpha():
        arr.append(newtext[i])
nums = {}
for i in range(len(arr)):
    num = 0
    for j in arr:
        if arr[i] == j:
            num+=1
            nums[arr[i]] = num
#keys = list(nums.keys()) #сортировка в алфавитном порядке
#keys.sort()
keys = list(nums.items()) #сортировка в порядке возрастания
keys.sort(key = lambda i: i[1])
for i in keys:
    #print(i, ':', nums[i])
    print(i[0], ':', i[1])

