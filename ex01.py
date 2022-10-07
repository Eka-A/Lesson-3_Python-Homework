# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import random

n = int(input('Введите число: '))
list = [random.randint(0, 10) for i in range(n)]

print(list)

sum = 0
i = 0

for i in range(len(list)):
    if i < n and i%2 != 0:
        sum += list[i]
        i += 1

print('Сумма элементов списка, стоящих на нечётной позиции:', sum)