# def my_decorator(func):
#     def do_some_staff():
#         print('Hello word!')
#         result = func()
#         print('Hello word!')
#         return result
#
#     return do_some_staff
#
#
# def my_func():
#     pass
#
#
# my_new_func = my_decorator(my_func)
# my_new_func()

# правильное или более распростнранённое описание декоратора
#
# def my_decorator(func):
#     def do_some_staff():
#         print('Hello word!')
#         result = func()
#         print('Hello word!')
#         return result
#
#
#     return do_some_staff
#
#
# @my_decorator
# def my_func():
#     pass
#
#
# my_func()

# from datetime import datetime
#
# time = datetime.now()
#
#
# def my_decorator(func):
#     def do_some_staff():
#         print(time)
#         return func()
#
#     return do_some_staff
#
#
# @my_decorator
# def my_func():
#     print('Juuuu')
#
#
# my_func()
#
# def my_func(a,b):
#     return print(list(range(a, b)))
#
# print(my_func(1,11))
#
#
# def my_decorator(func):
#     def do_some_staff():
#         list = func()
#         print(list)
#         # result_list = filter(lambda x: x % 2 == 0, func())
#         # print(result_list)
#         return func()
#     return do_some_staff
#
#
# @my_decorator
# def my_func(a,b):
#     return print(list(range(a, b)))
#
# my_func(1,10)

# def my_decorator(func):
#     def do_smth():
#         list = func()
#         new_list = [i for i in list if i % 2 == 0]
#         print(new_list)
#         return func(), new_list
#     return do_smth
#
#
# @my_decorator
# def myfunc():
#     list = [i for i in range(1, 11, 1)]
#     return list
#
#
# def my_decorator(func):
#     def do_smth(a, b):
#         result_list = list(filter(lambda x: x % 2 == 0, func(a, b)))
#         print(result_list)
#         return func(a, b)
#     return do_smth
#
#
# @my_decorator
#
#
# def my_func(a,b):
#     list_a = list(range(a, b))
#     return list_a
#
# my_func(1,11)

# my_file = open('text.txt')
# print(my_file.readline())
# my_file.close()

# my_file = open('text.txt')
# while True:
#     line = my_file.readline()
#     if not line:
#         break
#     print(line)
# my_file.close()

# ЗАДАЧА . напечатать
# 1 строку
# 5 строку
# первые 5 строк
# его строки с 1 по 2
# весь файл

# my_file = open('text.txt')
#
# for i in range(1, 10):
#     line = my_file.readline()
#     if i == 5:
#         print(line)
#     i += 1
# my_file.close()
# #######################
# sec_file = open('text.txt')
#
# i = 0
# while i < 5:
#     line = sec_file.readline()
#     print(line)
#     i += 1
#
# sec_file.close()
# #######################
# new_file = open('text.txt')
# def print_lines(a, b):
#     for i in range(1, 10):
#         line = new_file.readline()
#         if a <= i <= b:
#             print(line)
#         i += 1
#
# print_lines(2, 4)
# new_file.close()
# newnew_file = open('text.txt')
# #######################
# while True:
#     line = newnew_file.readline()
#     if not line:
#         break
#     print(line)
# newnew_file.close()

# my_file = open('text.txt')
# print(my_file.readlines())
# my_file.close()

# with open('text.txt') as my_file:
#     for line in my_file.readlines():
#         print(line)


# ЗДЕСЬ МЫ ПРИ ОТКРЫТИИ ПРОСТО ВЗЯЛИ И ЗАМЕНИЛИ ВСЁ ЧТО БЫЛО В ФАЙЛЕ И ПОТОМ ВЫЗВАЛИ ЕГО

# with open('text.txt', 'w') as my_file:
#     my_file.write('qwerty')
#
# with open('text.txt') as my_file:
#     for line in my_file.readlines():
#         print(line)

# with open('text.txt', 'a') as my_file:
#     my_file.writelines(['qwerty\n', 'asdf'])
#
# with open('text.txt') as my_file:
#     for line in my_file.readlines():
#         print(line)

# СОЗДАТЬ ТЕКСТОВЫЙ ФАЙЛ И ЗАПИСАТЬ В НЕГО 6 СТРОК. ЗАПИСЫВАЕМЫЕ СТРОКИ ВВОДЯТСЯ С КЛАВИАТУРЫ

# with open('text.txt', 'w') as myfile:
#     ind = 1
#     while ind < 7:
#         c = input('str:  ')
#         ind += 1
#         myfile.write( c + '\n')
#
# with open('text.txt') as my_file:
#     for line in my_file.readlines():
#         print(line)

# В КОНЕЦ СУЩЕСТВУЮЩЕГО ТЕКСТВООГО ФАЙЛА ЗАПИСАТЬ ТРИ НОВЫЕ СТРОКИ ТЕКСТА. ЗАПИСЫВАЕМЫЕ СТРОКИ ВВОДЯТСЯ С КЛАВИАТУРЫ

# with open('text.txt', 'a') as myfile:
#     ind = 1
#     while ind <= 3:
#         c = input('str:  ')
#         ind += 1
#         myfile.writelines([c + '\n'])
#
# with open('text.txt') as my_file:
#     for line in my_file.readlines():
#         print(line)

# ЗАДАНИЕ 10.04
# ИМЕЕТСЯ ТЕКСТОВЫЙ ФАЙЛ. ПЕРЕПИСАТЬ В ДРУГОЙ ФАЙЛ ВСЕ ЕГО СТРОКИ С ЗАМЕНОЙ В НИХ СИМВОЛА 0 НА СИМВОЛ 1 И НАОБОРОТ

# with open('text.txt') as my_file:
#     data = my_file.readlines()
#
#
# with open('izmen.txt', 'w') as new_file:
#     for x in data:
#         for i in x:
#             if i == '0':
#                 i = '1'
#             elif i == '1':
#                 i = '0'
#             new_file.write(i)
#
# with open('izmen.txt') as my_file_new:
#     for line in my_file_new.readlines():
#         print(line)

# 10/05
# ИМЕЕТСЯ ТЕКСТОВЫЙ ФАЙЛ. ВСЁ ЧЕТНЫЕ СТРОКИ ЭТОГО ФАЙЛА ЗАПИСАТ ВО ВТОРОЙ ФАЙЛ. А НЕЧЁТНЫЕ - ВТРЕТТИЙ ФАЙЛ.
# ПОРЯДОК СЛЕДОВАНИЯ СТРОК СОХРАНЯЕТСЯ