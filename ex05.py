# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

from unittest import result

n = int(input('Введите число: '))

def fib(n):
    if n in [1,2]:
        return 1
    if n < 0:
        return fib(-n) * (-1) ** (-n+1)
    else:
        return fib(n-1) + fib(n-2)

result = []

for i in range (n):
    result.append(fib(-n+i))

for i in range(n+1):
    result.append(fib(i))

print(result)