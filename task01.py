# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input('Введите натуральную степень k: '))
my_list = ['']
coefficient = random.randint(1, 100) #коэффициент при x^k должен быть > 0 исходя из условия и примера
if coefficient != 1:
    my_list[0] = (f'{coefficient}*')
if k != 1:
    my_list[0] += (f'x^{k}')
else:
    my_list[0] += (f'x')
for i in range(k - 1, 0, -1):
    coefficient = random.randint(0, 100)
    if coefficient > 1:
        match i:
            case 1:
                my_list.append(f'{coefficient}*x')
            case _:
                my_list.append(f'{coefficient}*x^{i}')
    elif coefficient == 1:
        match i:
            case 1:
                my_list.append(f'x')
            case _:
                my_list.append(f'x^{i}')
coefficient = random.randint(0, 100)
if coefficient != 0:
    my_list.append(f'{coefficient}')
result = ' + '.join(my_list)
result += ' = 0'
file = open('text01.txt', 'w')
file.write(result)
file.close()