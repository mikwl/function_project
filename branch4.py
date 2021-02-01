# СОЗДАТЬ Ф-Ю КОТОРАЯ ПРИНИМАЕТ НА ВХОД НЕОПРЕДЕЛЁННОЕ КОЛ-ВО АРГУМЕНТОВ И ВОЗВРАЩАЕТ ИХ СУММУ И МАКСИМАЛЬНОЕ ИЗ НИХ

def my_func(*args):
    summary = 0

    for i in args:
        summary += i
        stroka = list(args)
        stroka = list.sort
        last = print(stroka[-1])
        last = str(last)
        return summary, last

print(my_func(4, 5, 7, 8, 0, 1, 4), ' ')