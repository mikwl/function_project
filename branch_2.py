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
def factorial(n): #david
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
a = int(input('Enter some number: '))
print(factorial(a))

# nastya
def fact(n):
    ind = 0
    res = 1
    while ind < n:
        ind +=1
        res *= ind
    print(res)
    return res
fact(5)

#kate
def factorial(n):
    n = int(input('n = '))
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    print(f'Factorial is {fact}')
    return fact

factorial(1)