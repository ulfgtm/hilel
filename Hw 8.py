#1

persons = [{'name': 'John', 'age': 15},
            {'name': 'Jack', 'age': 45},
            {'name': 'Valentin', 'age': 45}]
year = []
min_year = []

name_1 = []
max_name = []

for years in persons:
    year.append(years['age'])

for years_min_name in persons:
    if years_min_name['age'] == min(year):
        min_year.append(years_min_name['name'])

for name_2 in persons:
    name_1.append(len(name_2['name']))

for name_max_long in persons:
    if len(name_max_long['name']) == max(name_1):
        max_name.append(name_max_long['name'])

sum_year = sum(year)/ len(year)

#2
my_dict = {1:2, 3:4, 5:6}
my_dict_2 = {1:2, 3:4, 7:8}

key_dict_1_2 = list(set(my_dict).intersection(my_dict_2))


key_dict_1_unique = list(set(my_dict).difference(my_dict_2))

new_key_dict_1 = {dict_key_1: my_dict[dict_key_1] for dict_key_1 in key_dict_1_unique}

dict_3 = list(set(my_dict).symmetric_difference(my_dict_2))
dict_finish = {dict_finish_1:(my_dict | my_dict_2)[dict_finish_1] for dict_finish_1 in dict_3}
dict_finish.update({key: [my_dict[key], my_dict_2[key]] for key in key_dict_1_2})













