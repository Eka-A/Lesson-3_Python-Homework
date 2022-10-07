#  Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import math
from unittest import skip

def mult_lst(lst):
    l = len(lst)//2 + 1
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_lst)

lst = [2, 3, 4, 5]
print(lst)
mult_lst(lst)