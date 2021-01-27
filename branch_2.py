# # def factirial(number):
# #     number = int(input('Enter some number: '))
# #     i = 0
# #     for i in range(number):
# #         a = i * (i + 1)
# #         print(a)
# #         f = int
# #         f += a
# #     print(f)
# #
# def factorial(n): #david
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# a = int(input('Enter some number: '))
# print(factorial(a))
#
# # nastya
# def fact(n):
#     ind = 0
#     res = 1
#     while ind < n:
#         ind +=1
#         res *= ind
#     print(res)
#     return res
# fact(5)
#
# #kate
# def factorial(n):
#     n = int(input('n = '))
#     fact = 1
#     while n > 0:
#         fact *= n
#         n -= 1
#     print(f'Factorial is {fact}')
#     return fact
#
# factorial(1)

# def my_format(string, char='!'):
#     result_string = f'{char}{string}{char}'
#     return result_string
#
# print(my_format(4))

# def print_list(*args):
#     print(args)
# print_list(1,2,3,4)

# def numbers_list(*args): МОЯ НЕПРАВИЛЬНАЯ ЛОГИКА!!!!
#     i = int
#     summ = 0
#     n = 0
#     while i > 0:
#         i -= 1
#         n += 1
#         summ += i * n
# print(numbers_list(input('Enter some arguments: ')))


# ????? СЧИТАЕТИ ЛИ ПРАВИЛЬНО?!
# def summ(*args):
#     summary = 0
#     n = 0
#     for i in args:
#         summary += i * args[n]
#         n += 1
#     print(summary)
#
#
# summ(4, 3, 2, 1)

def my_func(a, b):
    summ = a + b
    diff = a - b
    return summ, diff

summ, diff = my_func(4, 3)
print(summ, ' ', diff)


