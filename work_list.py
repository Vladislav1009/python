import datetime
from distutils.command.build_scripts import first_line_re 
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

def func (counter, is_max, is_min):
    if is_max == False:
        counter_max = max(counter.values())
        return print(counter_max)
    elif is_min == False:
        counter_min = min(counter.values())
        return print(counter_min)
    else:
        print('Вы не указали действие')
	


active = True 
while active:
	print( '0 - завершить работу\n','1 - калькулятор\n','2 - вывод даты и времени\n','3 - объеденение двух массивов\n', '4 - обработка словаря')
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
	else:
		print('Команда введена не верно')
print('Досвидания')
