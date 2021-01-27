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

def full_func (*args, **kwargs):
    print(args)
    print(kwargs)
full_func(1, 2, 3, a = 4, b = 5, c = 6)
print(full_func)

