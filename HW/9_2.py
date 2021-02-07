# Создать lambda функцию, которая принимает на вход неопределенное
# количество именных аргументов и выводит словарь с ключами удвоенной
# длины. {‘abc’: 5} -> {‘abcabc’: 5}

# old_dict = {'aa': 1, 'b': 2, 'cccc': 3}
# new_dict = {key + str(key): value for key, value in old_dict.items()}
# print(new_dict)

# name = ['ZHYZHA', 'GRYZHA', 'LYZHA']
# hello_name = lambda name: [f'Hello {i}' for i in name]
# print(hello_name(name))

key_new = lambda **kwargs: {key*2 : value for key, value in kwargs.items()}
print(key_new(abc=2, bbb=3, c=1))