import random
import string
#1


def new_my_list_return(my_list):
    new_list = []
    for index, symbol in enumerate(my_list):
        if not index % 2:
            new_list.append(symbol[::-1])
        else:
            new_list.append(symbol)
    return new_list
#2

def new_my_list(my_list):
    new_list = []
    for symbol_my_list in my_list:
        if not symbol_my_list[0].find('a'):
            new_list.append(symbol_my_list)
    return new_list

# 3

def new_my_list_task_3(my_list):
    new_list = []
    for symbol_my_list in my_list:
        if symbol_my_list.find('a') >= 0:
            new_list.append(symbol_my_list)
    return new_list

# 4

def new_my_list_task_4(my_list):
    new_list_str = []
    for string in my_list:
        if isinstance(string, str):
            new_list_str.append(string)
    return new_list_str

# 5
def new_my_list_task_5(my_list):
    new_list = []
    my_str = ''
    for symbol in my_str:
        if my_str.count(symbol) == 1:
            new_list.append(symbol)
    return new_list
# 6
def new_my_str_task_6(my_str_1,my_str_2):
    my_list = []
    intersection = my_set_1.intersection(my_str_2)
    for symbol in intersection:
        my_list.append(symbol)
    return my_list

# 7
def new_my_str_task_7(my_str_1,my_str_2):
    my_list = []
    for symbol in set(my_str_1 + my_str_2):
        if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
            my_list.append(symbol)
    return my_list

# 8

def my_email_random(names,domains):
    random_generete =''.join(random.choice(string.ascii_letters)for count in range(0, random.randint(5,7)))
    email_random = random.choice(names) + '.' + str(random.randrange(100,999)) + '@' +random_generete + '.' + random.choice(domains)
    return email_random



# 1.1
my_list = ['qwe', 'bmnb', 'sddf', 'wer']
new_list = new_my_list_return(my_list)

# 2.2
my_list = ['swe', 'bmnb', 'addf', 'war']
mew_list = new_my_list(my_list)

#3.3
my_list = ['swe', 'bmnb', 'addf', 'war']
new_list = new_my_list_task_3(my_list)

# 4.4

my_list = [1, 2, 3, "11", "22", 33]
new_list = new_my_list_task_4(my_list)

# 5.5
my_str = 'qeijqjklejqlac'
new_list =  new_my_list_task_5(my_list)

# 6.6
my_str_1 = 'qqwweerrj'
my_str_2 = 'qwejooll'
new_list = new_my_str_task_6(my_str_1,my_str_2)

# 7

my_str_1 = 'qqwweerrj'
my_str_2 = 'qwejooll'

new_list = new_my_str_task_7(my_str_1,my_str_2)

# 8

names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = my_email_random(names,domains)