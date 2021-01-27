# print('Hello world')

def my_func(a, b):
    summ = a + b
    print(f'{a} + {b} = {summ}')
    return summ
    # РЕТУРН НУЖНО ОНА ЗАПИСЫВАЕТ / ВОЗВРАЩАЕТ НАМ ЗНЧЕНИЕ И ЭТО ЗНАЧЕНИЕ МЫ МОЖЕМ ЗАПИСАТЬ В КАКУЮ-ТО ПЕРЕМЕННУЮ

my_func(4, 5)

my_func(10, 10)

my_func('lala', 'bebebe')

a = my_func(4, 5)
print(a)
