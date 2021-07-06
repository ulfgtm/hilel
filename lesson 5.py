# my_list_1 = [1, 2, 3, 4, 5]
# my_list_2 = [10, 20, 30, 40, 50]
#
# my_result = []
#
# min_len_lists = min(len(my_list_1), len(my_list_2))
#
# for index in range(min_len_lists):
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
# last_values_list_1 = my_list_1[min_len_lists:]
# last_values_list_2 = my_list_2[min_len_lists:]
#
# my_result = my_result + last_values_list_1 + last_values_list_2
#
# print(my_result)

# id() - номер обьекта в памяти

# my_list = [1, 2, 3]
# print(id(my_list))
# my_list = [2, 3, 4, 5]
# prind(id(my_list))
#
# my_list = [1, 2, 3]
#
# result = []
# print(id(result))
#
# result = result + my_list
# print(id(result))

# Генератор списков

# folders = []
# for digit in range(1, 20):
#     folder = f'/tmp/{digit}'
#     folders.append(folder)
# print(folders)

# folders = [f'/tmp/{digit}'for digit in range(1, 20)]
# print(folders)

# symbols = [ord(symbol) for symbol in 'eyueao']
# print(symbols)


# alhabet = [chr(ord_index)for ord_index in range(ord('a'), ord('z'))]
# alhabet = "".join(alhabet)
# print(alhabet)

# ножество Set не сохраняет порядок и все элименты уникальны

# new_set = {1,2,3,54,54,54}
# print(new_set)

# my_list = [1, 2, 2, 3, 5, 9]
# my_set = set(my_list)
# my_list_uniaue = list(my_set)
# print(my_list_uniaue)

# my_str = 'bla Bla car'
# my_str = my_str.lower()
# res_len = len(set(my_str))
# print(res_len)

# my_str = 'qqqqqqqqqqqqqqqqwwwwwwwwwwwwwwrrrrrrrrrrrrrrrrrrrrrrrrrr'
# for symbol in set(my_str):
#     print(symbol, my_str.count(symbol))

# my_str_1 = 'qwerty54512213'
# my_str_2 = 'qweertysd'
#
# my_set_1 = set(my_str_1)
# my_set_2 = set(my_str_2)
#
# inersection = my_set_1.intersection(my_set_2)
# print(inersection)
#
# union = my_set_1.union(my_set_2)
# print(union)
#
# difference = my_set_1.difference(my_set_2)
# print(difference)

# Словарь - dict Не сохраняет порядок, все ключи уникальны, остается последние зн.
# Ключи это любые неизменяемые обекты



# triangle = [[1, 1], [2, 3], [4, -2]]
# print(triangle[1][1])

# triangle = {"A":{"x":1, "y":1},
#             "B": {"x":2,"y":3},
#             "C": {"x":4,"y":-2}}
# print(triangle["B"]["y"])


test_dict = {1: 'qwerty'}
print(test_dict[1])