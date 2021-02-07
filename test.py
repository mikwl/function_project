# # print('Hello world')
#
# def my_func(a, b):
#     summ = a + b
#     print(f'{a} + {b} = {summ}')
#     return summ
#     # РЕТУРН НУЖНО ОНА ЗАПИСЫВАЕТ / ВОЗВРАЩАЕТ НАМ ЗНЧЕНИЕ И ЭТО ЗНАЧЕНИЕ МЫ МОЖЕМ ЗАПИСАТЬ В КАКУЮ-ТО ПЕРЕМЕННУЮ
#
# my_func(4, 5)
#
# my_func(10, 10)
#
# my_func('lala', 'bebebe')
#
# a = my_func(4, 5)
# print(a)

# def function(*args):
#     result = 0
#     for i in args:
#         result +=i
#         continue
#     result *= len(args)
#     return result
# print(function(1, 2, 3, 4))

# def sorting(*args):
#     summ = 0
#     n = 0
#     maxim = 0
#     for i in args:
#         summ += i
#         if i > args[-1] and i > maxim:
#             maxim = i
#         n += 1
#     return summ, maxim
#
#
# summ, maxim = sorting(10, 15, 35)
# print(summ, maxim)
#
# def my_func(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
# my_func(a = 5, b = 6)
#
# print(my_func)
#
# def full_func (*args, **kwargs):
#     print(args)
#     print(kwargs)
# full_func(1, 2, 3, a = 4, b = 5, c = 6)
# print(full_func)

# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# if a < b:
#     print(a)
# else:
#     print(b)
#
# a = int(input('Enter a: '))
# if a > 0:
#     print('sign(x) = 1')
# elif a > 0:
#     print('sign(x) = -1')
# else:
#     print('sign(x) = 0')

# import math
# a = float(input('Class A: ')) / 2
# a = math.ceil(a)
# b = int(input('Class B: ')) / 2
# b = math.ceil(b)
# c = int(input('Class C: ')) / 2
# c = math.ceil(c)
# print(a + b + c)

# a = int(input('Enter number: '))
# print(a % 10)

# a = int(input('A: '))
# b = int(input('B: '))
# i = 0
# if a < b:
#     for i in range(a, b + 1):
#         print(i)
# elif a == b:
#     print(a)
# else:
#     print('Enter new numbers A < B!')

# a = int(input('A: '))
# b = int(input('B: '))
# if a < b:
#     for i in range(a, b + 1):
#         print(i)
# else:
#     for i in range(a, b - 1, -1):
#         print(i)

# a = int(input('A: '))
# b = int(input('B: '))
# for i in range(a - (a + 1) % 2, b - b % 2, -2):
#     print(i)
#
# a = int(input('Enter A: '))
# b = int(input('Enter B: '))
# if a < b:
#     for i in range(a, b + 1):
#         print(i)
# else:
#     for i in range(a, b - 1, -1):
#         print(i)

# list_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# summary = 0
# for i in list_number:
#     summary += i
# print(summary)

# list_a = [i for i in range(5)]
# print(list_a)
# list_b = [i ** 2 for i in [1,2,3]]
# print(list_b)

# list_original = ['lalala', 'xaxaxa', 'papapa']
# list_reverse = list(reversed(list_original))
# print(list_reverse)

# names = ['Max', 'Helen', 'Alex', 'Misha']
# list_a = [name for name in names if 'a' in names]
# print(list_a)

# ДАН СПИСОК СЛОВАРЕЙ. КАЖДЫЙ СЛОВАРЬ ОПИСЫВАЕТ МАШИНУ(СЕРИЙНЫЙ НОМЕР И ГОД ВЫПУСКА)
# СОЗДАТЬ НОВЫЙ СПИСОК СО ВСЕМИ МАШИНАМИ

# dict_car = [{
#     'number_serial': '1923 CE-7',
#     'number_year': '1997'
# },
# {
#     'number_serial': '2548 XX-4',
#     'number_year': '2007'
# },
# {
#     'number_serial': '7777 EE-9',
#     'number_year': '2020'
# }]
#
# # print(dict_car)
#
# n = 2000

# list_dicts = [{'n': 1, 'y': 1993}, {'n': 2, 'y': 1995}, {'n': 3, 'y': 1998}, {'n': 4, 'y': 1959}, {'n': 5, 'y': 1994}]
# n = 1991
# list_b = [i for i in dict_car for i
# print(list_b)
#
# list_dicts = [{'n': 1, 'y': 1993}, {'n': 2, 'y': 1995}, {'n': 3, 'y': 1998}, {'n': 4, 'y': 1959}, {'n': 5, 'y': 1994}]
# n = 1991
# list_b = [i for i in list_dicts for k, v in i.items() if v > n]
#
# print(list_b)           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# from random import randint
# n = 3
# matrix = [[randint(1, 9) for j in range(n) for i in range(n)]]
# print(matrix)

# old_dict = {'aa': 1, 'b': 2, 'cccc': 3}
# new_dict = {key + str(len(key)): value for key, value in old_dict.items()}
# print(new_dict)


# old_dict = {'aa': 1, 'b': 2, 'cccc': 3}
# new_dict = {v: k for k,v in old_dict.items()}
# print(new_dict)

# def main():
#     pass
#
# if __name__ == '__main__':
#     main()

# ДАН СПИСОК ЧИСЕЛ. ПОСЧИТАТЬ СКОЛЬКО РАЗ ВСТРЕЧАЕТСЯ КАЖДОЕ ЧИСЛО. ИСПОЛЬЗОВАТЬ ФУНКЦИЮ
# ПОДСКАЗКА: ДЛЯ ХРАНЕНИЯ ДАННЫХ ИСПОЛЬЗОВАТЬ СЛОВАРЬ. ДЛЯ ПРОВЕРКИ НАХОЖДЕНИЯ ЭЛЕМЕНТА В СЛОВАРЕ ИСПОЛЬЗОВАТЬ
# МЕТОД get() ЛИБО ОПЕРАТОР in

# list_a = [1, 3, 5, 7, 54, 3, 5, 3, 7, 5, 3, 7, 2, 45, 54, 34, 3, 6, 3, 6, 8, 5, 3]
# n = 0
# diction_right_keys = {i: 1 for i in list_a}
#
# for k, v in diction_right_keys.items():
#     n = 0
#     for i in list_a:
#         if k == i:
#             n += 1
#     diction_right_keys[k] = n
#
# print(diction_right_keys)


# СОЗДАТЬ LAMBDA ФУНКЦИЮ КОТОРАЯ ПРИНИМАЕТ НА ВХОД СПИСОК ИМЕН И ВЫВОДИТ ИХ В ФОРМАТЕ "Hello, {name}" В ДРУГОЙ СПИСОК

# name = ['ZHYZHA', 'GRYZHA', 'LYZHA']
# hello_name = lambda name: [f'Hello {i}' for i in name]
# print(hello_name(name))

# result = map(lambda x: x ** 2, [1,2,3,4,5,6])
#
# print(list(result))

# ДАН СПИСОК ЧИСЛЕ. ВЕРНУТЬ СПИСОК ГДЕ КАЖДОЕ ЧИСЛО ПЕРЕВЕДЕНО В СТРОКУ
#  [5,3] -> ['5','3']

# result = map(lambda  x: str(x), [5,3])
# print(list(result))

# result = filter(lambda x: x % 2 == 0, [1,2,3,4,5,6])
# print(list(result))

# 9,04 ДАН СПИСОК ИМЁН ОТФИЛЬТРОВАТЬ ВСЕ ИМЕНА ГДЕ ЕСТЬ БУКВА К

# a = ['Kate', 'Sasha', 'Kristina', 'Vitya']
# result = filter(lambda x: 'K' in x, a)
# print(list(result))

# 9.05

# from functools import reduce
#
# items = [1,2,3,4,5]
# sum_all = reduce(lambda x,y: x + y, items)
#
# print(sum_all)

# 9.06

# ДАН СПИСОК ЧИСЛЕ НАЙТИ ПРОИЗВЕДЕНИЕ ВСЕХ ЧИСЕЛ, КРАТНОЕ ТРЁМ
# from functools import reduce
#
# items = [3, 10, 6, 20]
# umn_all = reduce(lambda x,y: x * y, list(filter(lambda x: x % 3 == 0, items)))
# print(umn_all)

