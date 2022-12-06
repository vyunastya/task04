# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты положительные и не равные 1
def data_from_file(name):
    file = open(name, 'r')
    my_list = file.read()
    my_list = my_list.replace("*x ", "*x^1 ")
    my_list = my_list.split(' ')
    file.close()
    return my_list
def create_dict(my_list):
    list_coefficient = []
    dictionary = {}
    for i in range(len(my_list) - 2):  # Отсекаю =0
        list_coefficient.append(my_list[i].split('*x^'))
    list_temp = list_coefficient[-1]
    list_temp.append('0')
    list_coefficient[-1] = list_temp
    for i in range(0, len(list_coefficient), 2):
        dictionary[int(list_coefficient[i][1])] = int(list_coefficient[i][0])
    return dictionary
def maxi(diction):
    res = -1  # Задаю априори меньшее значение
    for key in diction:
        if int(key) > res:
            res = int(key)
    return res
list_polynomial1 = data_from_file('text20.txt')
list_polynomial2 = data_from_file('text21.txt')
dict1 = create_dict(list_polynomial1)
dict2 = create_dict(list_polynomial2)
maximum1 = maxi(dict1)
maximum2 = maxi(dict2)
result = {}
if maximum1 > maximum2:
    maximum = maximum1
else:
    maximum = maximum2
    result
for i in range(maximum, -1, -1):
    result[i] = dict1.get(i, 0) + dict2.get(i, 0)
str_result = ''
for key, value in result.items():
    if value != 0 and key > 1:
        str_result += f' + {value}*x^{key}'
    elif key == 1:
        str_result += f' + {value}*x'
    elif key == 0:
        str_result += f' + {value}'
str_result += ' = 0'
result = str_result.replace(' + ', '', 1)
file = open('result2.txt', 'w')
file.write(result)
file.close()
