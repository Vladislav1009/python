import os # Импорт библиотеки OS

# Создание словаря, в котором значения (values) - это название файлов из директории. 
# В этих файлах указаны слова, символы, которые необходимо удалить из текста 
badchars_files_names = {           
    'arg': '_augmentations.txt',   
    'badchars': '_badchars.txt',   
    'stopwords': '_stopwords.txt'  
}
# Создание пустого вловаря, который будет хранить в себе символы, которые необходимо удалить
delete_symbols = {} 

# Создание цикла. Данный цикл работает следующим образом: цикл итерируется по словарю (badchars_files_names) и выводит пары (ключ, значения)
# присваивая их переменным цикла for, переменная path_file хранит в себе название файлов. Далее открываем файл и присваиваем переменной file
# Приводим переменную file к строковому значению (file_string). После чего добавляем в пустой словарь новые пары, где name_arg - это ключи 
# словаря badchars_files_names, а значения для ключей - это слова хранящиеся в файлах, которые открывает этот цикл (слова, которые надо удалять)
for name_arg, path_file in badchars_files_names.items():
    with open(path_file, mode='r', encoding='utf-8') as file:
        file_string = file.read()
        delete_symbols[name_arg] = file_string.split()


catalog_file = './beatles' # Создаем переменную, которой присваиваем относительный путь до директории beatles
file_in_catalog = os.listdir(catalog_file) # При помощи функции listdie библиотеки OS содержимое директории записываем в виде списка строк
music_text_dict: dict[str, str] = {} # Создаем пустой словарь, в который будем заносить пары в виде: key - название песни; value - слова песни

# В данном цикле выполняется открытие файлов из директории. Поочередно открывается текст песен и заносится в словарь music_text_dict, где 
# ключами словаря являются название файлов, а значения - это тексты песен
for file in file_in_catalog:
    with open(os.path.join(catalog_file, file), mode='r', encoding='utf-8') as file_in_folder:
        music_text_dict[file] = file_in_folder.read()

# Создается цикл, который будет итерироваться по словарю music_text_dict и при помощи внутренних циклов for будут производится операции со словарем
for name_file, music_text in music_text_dict.items():
    processed_music_text = music_text # Переменной присваивается значения словаря music_text_dict
    
# создается переменная arg_list, которой присваиваются пары из словаря delete_symbols с ключем 'arg'. Далее цикл итерирутся по парам словаря с ключамии
# arg и удаляет аргументы из текста в словаре processed_music_text. По аналогии удаляются и "плохие символы", и стоп слова.
    arg_list = delete_symbols['arg'] 
    for arg in arg_list:
        processed_music_text = processed_music_text.replace(arg, '')
        
    badchars_list = delete_symbols['badchars']
    for badchar in badchars_list:
        processed_music_text = processed_music_text.replace(badchar, '')

# Для того, что бы удалить стоп слова надо разбить уже очищенный текст по пробелам, после чего только выполнять чистку от стоп слов.
# Так как работа будет производится со массивом, то для чистки будем использовать функции списков. remove() - найти о очистить список от ()
    processed_music_text_list = processed_music_text.split()
    stopwords_list = delete_symbols['stopwords'] 
    for stopword in stopwords_list:
        if stopword in processed_music_text_list:
            processed_music_text_list.remove(stopword)
            
# В словарья передаем новые пары, где ключи словаря будут неизменными (название песен), а ключи - отредактированные тексты песен.    
    music_text_dict[name_file] = processed_music_text 
        
# print(music_text_dict['acrosstheuniverse.txt'])
# print(processed_music_text_list)

# Теперь необходимо подсчитать кол-во повторений слов и добавить их в список кортежей. Для этого необходимо проитерироваться по ключас словаря mesic_text_dict
word_count = {}
for word_dict in music_text_dict.values():
    print(word_dict)
    # if word_dict not in word_count:
    #     word_count[word_dict] = 

