import os



# path_file = 'C:\\Users\\Владислав Игоревич\\Desktop\\Python\\course-python\\2. base python\\2. Работа с файлами\\folder' #Создаю переменную и присваиваю ей путь к 
# # дериктории, который будет храниться в виде строки
# file_in_catalog = os.listdir(path_file)# list['str']. file_in_catalog хранит в себе список строк, где строка - это содержимое директории 
# result_list = []
# for name_file in file_in_catalog: # создаю цикл for который будет обходить список строк переменной file_in_catalog. name_file при каждой итерации будет меняться, поочередно перебирая 
#     # название файлов хранащихся в директории
#     with open(os.path.join(path_file, name_file), mode='r', encoding='utf-8') as name_files: # ???почему если я указываю кодировку, то python выдает ошибку???
#          # в данной строке происходит открытие файлов. В функцию open первым параметром передаю путь к файлу.
#         # путь к файлу получаю при помощи функции os.path.join(). Данная функция через "\" объеденяет то, что ей передали. В моем случае я передаю переменную path_file в которой хранится
#         # путь к директории, вторым параметром указываю переменную цикла for name_file, которая хранит в себе название файла, таким образом получается полный путь к файлу.
#         # была идея узнать путь к файлу, через функцию os.path.abspath(), она должна находить абсолютный путь к файлу. Но так не получилось, почему так и не разобрался.
#         name_files = name_files.read() # читаю содержимое файла. Содержимое файлов имеет тип str           
#         result_list += name_files.split() # в пустой список result_list добавляю строки из файлов преобразованные в список строк, где одна строка файла = одной строке в списке    
# # word_array = [] # создаю пустой массив, в который буду добавлять слова в одном экземпляре из массива result_list
# # count_array = [] # создаю пустой массив, в который буду добавлять кол-во слов содержащихся в массиве result_list
# # for word in result_list: # создаю цикл for, который будет проходить по массиву result_list 
# #    if word not in word_array: # создаю условие, которые будет добавлять в пустой массив(word_array) строки из массива result_list. Если слово повторяется, тогда оно повтороно не добавится
# #        word_array += [word] # добавляю слово в массив
# # for count_word in word_array: # создаю цикл, который будет подсчитывать слова в массиве result_list
# #     count_array += [result_list.count(count_word)] # в пустой массив добавляю кол-во слов в массиве. 
# # final = [tuple((word_arrayo))]
# dict_result = {}
# for word in result_list:
#     if word not in dict_result:
#         dict_result[word] = result_list.count(word)
# final = []
# for sorted_dict in sorted(dict_result.items(), key=lambda key_value: (key_value[1], key_value[0]), reverse = True): # тогда в обратной последовательности 
#     # сортируется весь словарь, мне надо только ключи
#     final += [sorted_dict]
# # print(final)   
catalog_task = 'C:\\Users\\Владислав Игоревич\\Desktop\\Python\\course-python\\2. base python\\2. Работа с файлами\\task_condition' # Путь к файлам, 
# в которых хранится доп. задание
list_task = os.listdir(catalog_task) # заношу в список название файлов из директории
delete_symbols = [] # переменная in_file хранит в себе все, что необходимо удалить из текста.
for str_file in list_task:
    with open(os.path.join(catalog_task, str_file), mode='r', encoding='utf-8') as stroki_file:
        stroki_file = stroki_file.read()
        delete_symbols += stroki_file.split()

catalog_file = 'C:\\Users\\Владислав Игоревич\\Desktop\\Python\\course-python\\2. base python\\2. Работа с файлами\\folder' 
file_in_catalog = os.listdir(catalog_file)
for files in file_in_catalog:
    with open(os.path.join(catalog_file, files), mode='r', encoding='utf-8') as file_in_folder:
        file_in_folder = file_in_folder.read()
        for symble in delete_symbols:
            if sym
# теперь мне надо соеденить два кода, у меня есть два списка: в котором хранится содержимое папок, где надо посчитать слова и список, где хранится от
# чего надо очсистить файл. Прежде чем дректорию с файлайми (где надо посчитать слова) перевести в список, надо при помощи цикла for и функции split
# очистить ее от лишних символов, слов. По сути надо еще превести все к одному регистру. После этого я смогу все посчитать.