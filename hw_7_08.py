# Написать функцию принимающая на вход
# неопределенным количеством аргументов и именованный
# аргумент mean_type. В зависимости от mean_type вернуть
# среднеарифметическое либо среднегеометрическое.
# Написать программу в виде трех функций.

def sr_g(args):
    summary = 1
    n = len(args)
    for i in args:
        summary *= i
    return pow(summary, 1/n)

def sr_a(args):
    summary = 0
    n = len(args)
    for i in args:
        summary += i
    return summary / n

def sr_choice(*args, mean_type):
    if mean_type == 'a':
        return sr_a(args)
    elif mean_type == 'g':
        return sr_g(args)

print(sr_choice(1, 10, 4, mean_type='g'))
print(sr_choice(1, 10, 4,  mean_type='a'))
