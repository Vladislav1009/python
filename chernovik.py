
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

def loadstring(fname):
    with open(fname, mode='r', encoding='utf-8') as file:
        file_str = file.read().replace(' ', '')
        file_array = file_str.split('\n') # либо метод splitlines()
        return print(file_array)

file_user = input('Укажите имя файла в котором удалить пробелы: ')
loadstring(file_user)


