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

list_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
summary = 0
for i in list_number:
    summary += i
print(summary)



