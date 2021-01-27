# def factirial(number):
#     number = int(input('Enter some number: '))
#     i = 0
#     for i in range(number):
#         a = i * (i + 1)
#         print(a)
#         f = int
#         f += a
#     print(f)
#
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
a = int(input('Enter some number: '))
print(factorial(a))


def fact(n):
    ind = 0
    res = 1
    while ind < n:
        ind +=1
        res *= ind
    print(res)
    return res
fact(5)