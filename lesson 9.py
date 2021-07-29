# import random
#
# value = random.randint(10, 20) #случайное число
# print(value)

from random import randint

# value = random.randint(10, 20) #случайное число
# print(value)

import random
# value = random.randint(10, 20)
# my_list = [1, 3, 4, 5]
# choice_from_list = random.choice(my_list)
# print(value, choice_from_list)


#shuffle меняет обьект! Нужен .copy


import random
point_A = {'x': random.randint(-10, 10),
            'y': random.randint(-10, 10)}

point_B = {'x': random.randint(-10, 10),
            'y': random.randint(-10, 10)}

point_C = {'x': random.randint(-10, 10),
            'y': random.randint(-10, 10)}

triangle_ABC = {'A': point_A,
                 'B': point_B,
                 'C': point_C}
print(triangle_ABC)