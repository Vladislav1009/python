# 2. Выполнить загрузку файла data_df.json (data/data_df.json) в DataFrame и выполнить следующие задачи:
#     - Вывести первые 10 элементов в консоль и предоставить фото результата
#     - Получить медиану, максимальную и минимальную сумму по стоимости заказа
#     - Вывести все строки, у которых почта пользователя равна "yandex_main@yandex.ru"

import pandas as pd
import numpy as np
import json 


with open('data_df.json', mode='r', encoding='utf-8') as file_json:
    json_python = json.load(file_json)
file_df = pd.DataFrame(json_python['data'])


email = 'yandex_main@yandex.ru'
df_email = file_df['user_email'].isin(['yandex_main@yandex.ru'])
print(df[df_email])
    




# # Вывести первые 10 элементов в консоль и предоставить фото результата
# first_ten = file_df[:10] 
# print(first_ten)
# # ////////////////////////////////////////////////////////////////////////////

# # Получить медиану, максимальную и минимальную сумму по стоимости заказа
# sort_summ = sorted(file_df['pay_summ'])
# len_summ = len(sort_summ)//2
# median_summ = sort_summ[len_summ]
# max_summ = file_df['pay_summ'].max()
# min_summ = file_df['pay_summ'].min()
# print('Максимальная сумма: ',max_summ)
# print('Минимальная сумма: ',min_summ)
# print('Медиана: ',median_summ)

# # ////////////////////////////////////////////////////////////////////////////

# # Вывести все строки, у которых почта пользователя равна "yandex_main@yandex.ru"

# email = 'yandex_main@yandex.ru'
