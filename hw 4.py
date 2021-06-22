#1
my_list = [150, 300, 500, 125, 70, 90]
for i in my_list:
    if i > 100 :
        print(i)

##############################

#2

my_list= [70, 80, 100, 300, 152]
my_results=[]
for i in my_list:
    if i > 100:
        my_results.append(i)

print(my_results)

#############################

#3

my_list = [1, 2, 3, 5]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1]+my_list[-2])
########################

#4

value = input("ВВедите число с точкой: ")
try:
    print(float(value)**-1)
except ValueError:
    print('Попробуй число: ')
except ZeroDivisionError:
    print("На ноль делить нельзя: ")

##############################
#5
my_string = '0123456789'
my_list = []
for symb_1 in my_string:
	for symb_2 in my_string:
		new_my_string = symb_1 + symb_2
		my_list.append(int(new_my_string))

print(my_list)
