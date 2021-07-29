
#1
my_list = ['qwe', 'bmnb', 'sddf', 'wer']
new_list = []

for index, symbol in enumerate(my_list):
    if not index % 2:
        new_list.append(symbol[::-1])
    else:
        new_list.append(symbol)
print(new_list)

# 2

my_list = ['swe', 'bmnb', 'addf', 'war']
new_list = []
for symbol_my_list in my_list:
    if not symbol_my_list[0].find('a'):
        new_list.append(symbol_my_list)
print(new_list)

#3

my_list = ['swe', 'bmnb', 'addf', 'war']
new_list = []

for symbol_my_list in my_list:
    if symbol_my_list.find('a') >=0:
        new_list.append(symbol_my_list)
print(new_list)

#4
my_list = [1, 2, 3, "11", "22", 33]
new_list = []

for string in my_list:
    if isinstance(string, str):
      new_list.append(string)
print(new_list)

5
my_str = 'qeijqjklejqlac'
new_list = []

for symbol in my_str:
    if my_str.count(symbol) == 1:
       new_list.append(symbol)
print(new_list)

#6

my_str_1 = 'qqwweerrj'
my_str_2 = 'qwejooll'

my_list = []

my_set_1 = set(my_str_1)

intersection = my_set_1.intersection(my_str_2)
for symbol in intersection:
    my_list.append(symbol)

print(my_list)

#7

my_str_1 = 'qqwweerrj'
my_str_2 = 'qwejooll'

my_list = []

for symbol in set(my_str_1 + my_str_2):
    if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) ==1:
        my_list.append(symbol)
print(my_list)

#8

my_dict = {'name': 'ivan',
           'surname': 'fedosov',
           'age': 24,
           'residence': {'County': 'Ukraine',
                         'city': 'dnioro',
                         'street': 'monitorna'},
           'work': {'availability': 'have',
                    'position': 'manager'}}
print(my_dict)

#9

my_dict = {'состовляющие': {'коржы': {'мука': 100,
                                      'молоко': 300,
                                      'яйца': 33},
                            'крем': {'сахар': 200,
                                     'масло': 150,
                                     'ваниль': 40,
                                     'сметана': 250,},
                            'глазурь': {'какао': 50,
                                        'сахар': 70,
                                        'масло': 100}}}
print(my_dict)













