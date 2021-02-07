# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
# это порядковый номер строки в списке. Использовать генератор списков.

key_new = lambda **args: {key: value for key, value in args.items()}
print(key_new(1, 2))

# list_a = [1, 3, 5, 7, 54, 3, 5, 3, 7, 5, 3, 7, 2, 45, 54, 34, 3, 6, 3, 6, 8, 5, 3]
# # list_b = list(range(0, (len(list_a) + 1) ))
# # print(list_b)
# for i in list_a:
# diction_right_keys = {key: i in list_a for key in list_a.items()}
# print(diction_right_keys)
