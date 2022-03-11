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


def wc3(fname, word_in_file):
    with open(fname, mode='r', encoding = 'utf-8') as file: #открываю файл для чтения
        read_file = file.read().split() # создаю переменную, которая будет читать файл одной строкой; для удобства работы преобразую строку в список строк (разделение по пробелу)
        value = read_file.count(word_in_file) # count() - в списке строк ищет строки "word" и считает их кол-во
        if word_in_file in read_file: # проверяю наличие строки в файле, если такая строка имеется, тогда переменной key присваиваю значение строки, которую искал
            key = word_in_file
        else:
            'Такого слова(символа, значения) нет в данном файле' # Если нужной строки не будет в файле консоль выведет текст, а не исключение
    new_dict = {key, value} # создаю словарь, где ключ и значение это переменные, которые нашел выше
    return print(new_dict) # возвращаю значение словаря
