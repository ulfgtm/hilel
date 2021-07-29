# функции сортировки

# my_list = [12, 3, 45, 23, -10, 1]
#
# sorted_list = sorted(my_list, reverse=True)

# my_str_list = ['John', 'Jack', 'Jacob', 'Violetta']
# sort_str_list = sorted(my_str_list)
# # print(sort_str_list)    по алфавиту
#
# sort_str_list = sorted(my_str_list, key=len)
# print(sort_str_list)



# def sort_by_price(price_dict):
#     price = price_dict['price']
#     name = price_dict['product']
#     return price, name
#
# price_list = [{'product': 'milk', 'price': 23},
#               {'product': 'ice-cream', 'price': 18},
#               {'product': 'meat', 'price': 120},
#               {'product': 'Coca-Cola', 'price': 10},
#               {'product': 'Pepsi-Cola', 'price': 10},
#               ]
#
# sorted_price_list = sorted(price_list, key=sort_by_price)
# print(sorted_price_list)

# def sort_by_len_and_name(name):
#     return len(name), name
#
# my_str_list = ['John', 'Jack', 'Jacob', 'Violetta']
#
# sort_str_list = sorted(my_str_list)
# print(sort_str_list)
#
# sort_str_list = sorted(my_str_list, key=sort_by_len_and_name)
# print(sort_str_list)

# Регулярные выражения

# import re
#
# my_string = 'dsknjfsdjknfsj, zxb 127.0.0.1, safdsdfdsfsf, 200.0.23.12.201:5400, dsfsdfsdfsdfsdf'
#
# template = r'\d+'
#
# template2 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
#
# result = re.findall(template2, my_string)
# print(result)

# Практика

import random
import string

import string

def generete_string(min_limit=50, max_limit=100):
    len_str = random.randint(min_limit, max_limit)
    res_str = ''.join([random.choice(string.ascii_lowercase)for _ in range(len_str)])
    return res_str


def choice_transform(word):
    word = word.capitalize()
    return word


def tranform_str_by_words(some_str):
    new_words = []
    words = some_str.split()
    for word in words:
        word = choice_transform(word)
        new_words.append(word)
    return ' '.join(new_words)

def insert_spaces(some_str):
    go_jump = True
    total_index = 0
    some_list = list(some_str)
    while go_jump:
        jump_index = random.randint(1, 10)
        current_index = total_index + jump_index
        if current_index < len(some_list):
            some_list[current_index] = ' '
            total_index += jump_index
        else:
            go_jump = False

    return "".join(some_list)


def transform_str(some_str):
    some_str = insert_spaces(some_str)
    some_str = tranform_str_by_words(some_str)
    return some_str


rand_str = generete_string()
tr_str = transform_str(rand_str)
print(tr_str)