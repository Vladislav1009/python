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

# # 5. Очистка слов | <b> СРЕДНЕ </b>

# # Написать функцию cleanup(text, badchars), выполняющую очистку текста,
# # заданного параметром text от символов, перечисленных в парамтре badchars.

# # ```python
# # def cleanup(text, badchars):
# #     # ENTER YOUR CODE HERE
# #     return # ENTER YOUR CODE HERE

# # # Проверка работоспособности функции cleanup().
# # print(cleanup('hello,\tworld!\n', '\n \t'))
# # print(cleanup('hello,\tworld!\n', ['\n', ' ', '\t']))
# # ```

# def cleanup(text: str, badchars):
#     text = text.replace(badchars, '')
#     text = text.replace(badchars, '')
#     return text

# # Проверка работоспособности функции cleanup().
# print(cleanup('hello,\tworld!\n', '\n \t'))
# print(cleanup('hello,\tworld!\n', ['\n', ' ', '\t']))


   
def cleanup(text, badcharp):
    for simbl in badcharp:
        text = text.replace(simbl, '')
    return text

text = input('Введите текст, который необходимо отредактировать: ')
badcharp = input('Через запятую укажите символы, которые необходимо удалить. Например: "-,=,!" ').split(',')
res_cleanup = cleanup(text, badcharp)

