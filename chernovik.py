
# 6. Построчная очистка файла от лишних символов | <b> СРЕДНЕ </b>

# Написать функцию loadstrings(fname), которая возвращает очищенный от пробелов
# список строк файла с именем fname.

# ```python
# def loadstrings(fname):
#     # ENTER YOUR CODE HERE
#     return # ENTER YOUR CODE HERE

# lines = loadstrings('lines.txt')
# ```

# def loadstring(fname):
#     with open(fname, mode = 'r', encoding = 'utf-8') as file:
#         file_list = file.readlines()
#         file_str = ''
#         for line in file_list:
#             file_str += line.rstrip()
#         file_str_1 = file_str.replace(' ', '')
#     return print(file_str_1)


# name_file = input('Введите имя файла: ')
# fname = loadstring(name_file)

# def loadstring(fname):
#     with open(fname, mode='r', encoding='utf-8') as file:
#         file_str = file.read().replace(' ', '')
#         file_array = file_str.split('\n') # либо метод splitlines()
#         return print(file_array)

# file_user = input('Укажите имя файла в котором удалить пробелы: ')
# loadstring(file_user)

# with open('test.txt', mode='r', encoding = 'utf-8') as file:
#         nchars = len(file.read())
#         nlines = len(nchars.split('\n'))
#         nwords = len(nchars.split(' ')) + 1


        
        

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




# def wc3(fname):
#     with open(fname, mode='r', encoding = 'utf-8') as file: #открываю файл для чтения
#         read_file = file.read().split() # создаю переменную, которая будет читать файл одной строкой; для удобства работы преобразую строку в список строк (разделение по пробелу)
#         value = read_file.count(word_in_file) # count() - в списке строк ищет строки "word" и считает их кол-во
#         if word_in_file in read_file: # проверяю наличие строки в файле, если такая строка имеется, тогда переменной key присваиваю значение строки, которую искал
#             key = word_in_file
#         else:
#             'Такого слова(символа, значения) нет в данном файле' # Если нужной строки не будет в файле консоль выведет текст, а не исключение
#     new_dict = {key, value} # создаю словарь, где ключ и значение это переменные, которые нашел выше
#     return print(new_dict) # возвращаю значение словаря


# with open('lines.txt', 'r', encoding = 'utf-8') as file:
#     nlines = 0
#     nchars = 0
#     for line in file:
#         nlines += 1
#         nchars = len(line)
#     print(nlines, ';', nchars)
#     # file_array = file.split()
#     # print(file)

