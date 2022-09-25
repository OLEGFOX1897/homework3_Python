# homework 3
# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# from my_function import input_list
# inp_list=input_list(0) # общий список для решения 1 и 2 задач
# sum_el=0 #сумма эл для решения 1 задачи
# out_list2=[] #выходной список для 2 задачи
# for ind in range(0,len(inp_list)-1):
#     if ind//2!=ind/2:
#         sum_el=sum_el+inp_list[ind]
#     if len(inp_list)/2==len(inp_list)//2 and ind<len(inp_list)//2:
#         out_list2.append(inp_list[ind]* inp_list[len(inp_list)-1-ind])
#     elif len(inp_list)/2!=len(inp_list)//2 and ind<len(inp_list)//2+1:
#         out_list2.append(inp_list[ind]* inp_list[len(inp_list)-1-ind])	
# print(f'Сумма элементов стоящ на неч местах равна = {float(sum_el)}')
# print(f'Решение 2 задачи: {out_list2}')

# # второй вариант решения 1 задачи (можно запускать одновременно)

# print(f'Массив из нечетных элементов: {inp_list[1::2]}')
# print(f'Их сумма равна: {sum(inp_list[1::2])}')


# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91
# task 1 добавь комменты
# from my_function import input_list, num_frac, min_max_list
# print('Задайте список из вещественных чисел')
# inp_list=input_list(0)
# out_list=[]

# for ind in inp_list:
#     out_list.append(num_frac(ind))

# print(f'Cписок из дробных частей {out_list}')
# print(f'Максимум={min_max_list(out_list,1)} Минимум={min_max_list(out_list,0)}')
# print(f'Их разница delta={round(min_max_list(out_list,1)-min_max_list(out_list,0),2)}')
  

# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# num = int(input())
# rem = ''
# while num > 0:
#     rem = str(num % 2) + rem
#     num = num // 2
 
# print(f'{num} - >{rem}')


# l = []
# def convert(num):
#     ''' рекурсия '''
#     if (num == 0):
#         return 1
#     dig = num % 2
#     l.append(dig)
#     convert(num // 2)
# rem = int(input("Введите число: "))
# convert(rem)
# print()
# l.reverse()
# for i in l:
#     print(i,end=' ')

# Задача №5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# from my_function import inp_num, revers_list
# list_fib_right=[]
# list_fib_left=[]
# list_fib=[]

# num=inp_num(1)

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# for ind in range(1,num+1):
#     list_fib_right.append(fib(ind))
# list_fib_left=revers_list(list_fib_right)

# for ind in range(1,len(list_fib_left)-1,2):
#     list_fib_left[ind]=list_fib_left[ind]*(-1)
# list_fib_left.append(0)
# list_fib=list_fib_left+list_fib_right
# print(list_fib)

