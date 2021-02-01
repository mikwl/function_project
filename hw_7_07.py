# Создать функцию, которая принимает на вход
# неопределенное количество именных
# аргументов и выводит на экран те из них,
# длина ключа которых четна.

def keys_even(**kwargs):
    for key, value in kwargs.items():
        if len(key) % 2 != 0:
            continue
        else:
            print(f'{key}:\'{value}\'')


keys_even(aaa=15, bbb=132, ccc=178, name='Lalala')
