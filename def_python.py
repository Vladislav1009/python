# # 4. Чтение из файла N строк | <b>ЛЕГКО</b>

# # Написать функцию head(fname, n), которая принимает имя файла fname 
# # и количество требуемых строк n и выводит на экран первые n строк файла;
# # если n не задано, то на экран выводятся 5 строк.

# # Примечание: при решении задачи размерами файла принебречь.

# # ```python
# # def head(fname, n=5):
    
# #     # ENTER YOUR CODE HERE

# # head('beatles.txt')
# # ```

# # <i>*** Добавить в систему УКС в виде команды ***</i>

def head(fname, n=5):
    with open(fname, mode='r', encoding='utf-8') as file:
        # if not n:
        #     n = 5

        counter = 0 
        for line in file:
            if counter >= int(n) + 1:
                break   
            print(line, end = '>>>') 
            counter += 1
    print('')

# 7. Чтение всех слов из файла | <b> СЛОЖНО </b>

# Написать функцию wc3(fname), которая читает файла с именем fname и возвращает 
# словарь вида {word: count},
# где 
#    - word - слово из текстового файла, 
#    - count - частота встречаемости слова word.

# ```python
# def wc3(fname):
#     # ENTER YOUR CODE HERE 
#     return # ENTER YOUR CODE HERE

# wc3('poem.txt')

# def wc3(fname): # создаю функцию, которая на вход получает файл 
#     with open(fname, mode='r', encoding='utf-8') as file: # jоткрываю файл для чтения
#         file = file.read().replace(',', ' ') # присваиваю переменной содержимое файла, type str. И при помощи функции replace() очищаю содержимое от запятых
#         file = file.split() # для удобства работы содержимое файла преобразую из типа str(строка) в тип данных list(сипсок)
#         dict_result = {} # создаю пустой словарь, который по итогу будет возвращать функция
#         for words in file: # создаю цикл for с переменной word. Цикл работает следующим образом: переменной words присваивается значение из списка file с нулевым индексом. filt[0]
#             if words not in dict_result: # Черех условие if проверяю наличиние перменной цикла words в словаре dict_result. Если переменной word в словаре нет, тогда выполняется
#                 # следующие действие: 
#                 dict_result[words] = file.count(words) #в словарь dict_result создается ключ, который равен переменной цикла words (dict_result[words]). 
#                 # К этому ключу надо присвоить значение, которое будет равно кол-ву повторений символов в списке. Для этого использую функцию count, 
#                 # которая позволяет посчитать кол-во конкретных символов в списке. в функцию count() передаю значение переменной, которое хранится в переменной цикла word ()
#                 # И питон считает сколько в списке file хранится переменных с значением words
#     return dict_result # функция возвращает словарь, который содержит key в виде символов и value в виде кол-во повторений этих символов.

def wc3(fname):
    with open(fname, mode='r', encoding='utf-8'):

# 8. Анализ файла | <b> СЛОЖНО </b>
 
# Написать функцию wc1(fname), которая анализирует содержимое файла 
# с именем fname и возвращает кортеж (nlines, nwords, nchars),
# где:
#    - nlines - количество строк, 
#    - nwords - количество слов (слова разделяются пробелом),
#    - nchars - количество символов (включая все типы пробельных символов).

# ```python
# def wc1(fname):
#     # ENTER YOUR CODE HERE
#     return nlines, nwords, nchars

# wc1('test.txt')
# ```

def wc1(fname):
    with open(fname, mode='r', encoding = 'utf-8') as file:
        nchars = len(file.read()) # читаю информацию из файла (тип str), и подсчитываю кол-во символов в файле
        nlines = len(nchars.split('\n')) # переменную nchars содержит строку в которой хранится содержимое файла, эту строку разбиваю по '\n'. после чего создается список строк, и кол-во строк в массиве равно кол-ву строк в файле
        nwords = len(nchars.split(' ')) + 1 # считаю кол-во пробелов в файле, так как слов в файле больше чем пробелов на 1, то добавляю 1
    return print(nlines, nwords, nchars)



# 9. "combine wordcounts" | <b> СЛОЖНО </b>

# Написать функцию combine_wc([wc1, wc2]), которая на основе список из словарей
# - результатов работы функции wordcount, содержащих пары (word: count), -
# создаёт новый словарь пар (word: count), по следующему правилу: 

# Если слово word присутствует только в одном из словарей wc1 или wc2,
# то оно добавляется в результирующий словарь с соответствующим значением count. 
 
# Если слово word присутствует в обоих словарях wc1 и wc2,
# то в результирующий словарь оно добавляется частотой count,
# равной сумме частот wc1[word] + wc2[word].

# ```python
# def combine_wc(list_dicts):
#     return pass

# words1 = {'hello': 1, 'world': 2, 'j': 1}
# words2 = {'word': 1, 'world': 3, 'j': 1}

# print(combine_wc([words1, words2]))

### 1й вариант решения задачи. Но при таком решении будет не удвлетворительный ответ в случае если я передам массив с 3мя словарями. Либо надо будет прописывать 3й цикл for,
### который будет проходить по 3му элементу массива

# def combine_wc(list_dict):
#     dict_result = {}
#     for key, value in list_dict[0].items():
#         if key not in dict_result:
#             dict_result[key] = value
    
#     for key, value in list_dict[1].items():
#         if key not in dict_result:
#             dict_result[key] = value
#         else:
#             dict_result[key] += value
#     return dict_result


def combine_wc(dict_result, dict_process):
    for key, value in dict_process.items():
        if key not in dict_result:
            dict_result[key] = value
        else:
            dict_result[key] += value
    return dict_result

def wordcount(list_dict):
    dict_result = {}

    for dict_process in list_dict:
        dict_result = combine_wc(dict_result, dict_process)
    
    # dict_result = combine_wc(dict_result, list_dict[0])
    # dict_result = combine_wc(dict_result, list_dict[1])
    # dict_result = combine_wc(dict_result, list_dict[2])
    return print(dict_result)

words1 = {'hello': 1, 'world': 2, 'j': 1}
words2 = {'word': 1, 'world': 3, 'j': 1}
words3 = {'word': 56, 'world': 12}



