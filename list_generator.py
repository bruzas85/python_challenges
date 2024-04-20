'''Работа с генераторами списков'''

import random
lst = [random.randint(-10, 10) for i in range(1, 20)]
print(lst)
lst_1 = [abs(elem) for elem in lst] # функция abs отбрасывает минусы
print(lst_1)

a = input('Enter numbers: ').split()
a = [int(i) for i in a]
print(a)

lst_2 = [(i, j) for i in 'abc' for j in [1, 2, 3]]
print(lst_2)