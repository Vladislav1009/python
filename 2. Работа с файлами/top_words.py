import os


badchars_files_names = { 
    'arg': '_augmentations.txt', 
    'badchars': '_badchars.txt', 
    'stopwords': '_stopwords.txt'
}
delete_symbols = {} # переменная in_file хранит в себе все, что необходимо удалить из текста.

for name_arg, path_file in badchars_files_names.items():
    with open(path_file, mode='r', encoding='utf-8') as file:
        file_string = file.read()
        delete_symbols[name_arg] = file_string.split()


catalog_file = './beatles'
file_in_catalog = os.listdir(catalog_file)
music_text_dict: dict[str, str] = {}

for file in file_in_catalog:
    with open(os.path.join(catalog_file, file), mode='r', encoding='utf-8') as file_in_folder:
        music_text_dict[file] = file_in_folder.read()


for name_file, music_text in music_text_dict.items():
    processed_music_text = music_text
    
    arg_list = delete_symbols['arg'] 
    for arg in arg_list:
        processed_music_text = processed_music_text.replace(arg, '')
        
    badchars_list = delete_symbols['badchars']
    for badchar in badchars_list:
        processed_music_text = processed_music_text.replace(badchar, '')
        
    processed_music_text_list = processed_music_text.split()
    stopwords_list = delete_symbols['stopwords'] 
    for stopword in stopwords_list:
        if stopword in processed_music_text_list:
            processed_music_text_list.remove(stopword)
        
    music_text_dict[name_file] = processed_music_text
        
# print(music_text_dict['acrosstheuniverse.txt'])
# print(processed_music_text_list)

list_tuple = [('w', 2), ('a', 5), ('g', 5)]

list_tuple.sort()

print(list_tuple)