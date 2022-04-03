# Это версия Саши, мои варианты реализации этой программы в черновике. 

import os

def wop_words2(folder, n=5):
    
    badchars_files_names = { 
        'arg': '_augmentations.txt', 
        'badchars': '_badchars.txt', 
        'stopwords': '_stopwords.txt'
    }
    delete_symbols = {} 

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
            
    word_count = {}
    for word_dict in music_text_dict.values():
        list_word_dict = word_dict.split()
        for word_str in list_word_dict:
            if word_str not in word_count:
                word_count[word_str] = 1
            else:
                word_count[word_str] += 1
    list_dict = list(word_count.items())
    list_dict = sorted(list_dict, key=lambda x: x[0], reverse=False)
    list_dict = sorted(list_dict, key=lambda x: x[1], reverse=True)
    print(list_dict[:n+1:])