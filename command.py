import datetime

from def_python import head

from def_python import wc3
 

def calc(a, b, opr):
	if opr == '+':
		return print(a + b)
	elif opr == '-':
		return print(a - b)
	elif opr == '/':
		return print(a / b)
	elif opr == '*':
		return print(a * b)
	else:
		return 'Неверная операция'

def getDatetime(form):
	data_time = datetime.datetime.now()
	return data_time.strftime(form)

def array(a, b, c):
	if c == 'first':
		return print(a+b) 
	elif c == 'last':
		return print(b+a)
	else:
		return 'Неверно введена команда'

def func(counter, is_max, is_min):
    if is_max == False:
        counter_max = max(counter.values())
        return print(counter_max)
    elif is_min == False:
        counter_min = min(counter.values())
        return print(counter_min)
    else:
        print('Вы не указали действие')
		
def cleanup(text, badcharp):
    for simbl in badcharp:
        text = text.replace(simbl, '')
    return text
def loadstring(fname):
    with open(fname, mode='r', encoding='utf-8') as file:
        file_str = file.read().replace(' ', '')
        file_array = file_str.split('\n') # либо метод splitlines()
        return print(file_array)
	


active = True 
while active:
	print( '0 - завершить работу\n','1 - калькулятор\n','2 - вывод даты и времени\n','3 - объеденение двух массивов\n', '4 - обработка словаря\n', '5 - работа с файлами\n', '6 - удаление символов\n', '7 - удаление пробелов в файле и создание списка строк\n', '8 - поиск слова(значения) в файле\n')
	comand = int(input('Какую команду ввести? '))
	if comand == 0:
		active = False

	elif comand == 1:
		a, b, opr = input('Введите а b opr(+, -, *, /). Например: 1 3 *: ').split() # split - разбивает массив по пробелам
		res = calc(int(a), int(b), opr)  

	elif comand == 2:
		form_data = input('Формат вывода даты и времени(можно пропустить): ')
		form_data = form_data if form_data else 'We are the %d, %b %Y'
		data = getDatetime(form_data)
		print(f'Актуальная дата и время: {data}')
	
	elif comand == 3:
		diapazon_a_1, diapazon_a_2 = input('Введите чезе пробел диапазон для массива "а": Например:1 5: ').split()
		diapazon_b_1, diapazon_b_2 = input('Введите чезе пробел диапазон для массива "b": Например:6 9: ').split()
		last_first = input('С какого массива начать? first = a; last = b ' )
		array_a = list(range(int(diapazon_a_1), int(diapazon_a_2) + 1))
		array_b = list(range(int(diapazon_b_1), int(diapazon_b_2) + 1))
		result = array(array_a, array_b, last_first)

	elif comand == 4:
		is_max, is_min = input().split()
		counter  = {
		'key_1': 1,
		'key_2': 10,
		'key_3': -14
		}
		result_func = func(counter, int(is_max), int(is_min))

	elif comand == 5:
		file_name = input('Название файла: ')
		n = int(input('Какое кол-во строк вывест? '))
		head(file_name, n=n)

	elif comand == 6:
		text_user = input('Введите текст, который необходимо отредактировать: ')
		badcharp_user = input('Через запятую укажите символы, которые необходимо удалить. Например: "-,=,!" ').split(',')
		cleanup(text_user, badcharp_user)

	elif comand == 7:
		file_user = input('Укажите имя файла в котором удалить пробелы: ')
		loadstring(file_user)
	
	elif comand == 8: 
		file_user = input('Введите название файла ')
		word_in_file = input('Что найти в указанном файле? ')
		wc3(file_user, word_in_file)
		

	else:
		print('Команда введена не верно')
print('Досвидания')
