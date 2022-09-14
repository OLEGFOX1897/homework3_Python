# Задача 1
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет
# day=int(input('Введите день недели (от 1 до 7) ='))
# if day==6 or day==7:
#     print(day,'-> да')
# else:
#     print(day,'-> нет')   

# Задача 2
# Напишите программу для. проверки истинности утверждения (X ⋁ Y ⋁ Z) = X ⋀ Y ⋀ Z для всех значений предикат.



# Задача 3
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
# плоскости, в которой находится эта точка (или на какой оси она находится).

# print ('Введите координаты точки на плоскости X и Y (не равные 0)')
# ordinatY=float(input("Y= "))
# abscisaX=float(input('X= '))
# if ordinatY==0 and abscisaX==0:
#     print('Неправильный ввод! Координаты точки равны нулю')
# elif ordinatY>0 and abscisaX>0:
#     print('X= ', abscisaX, 'Y= ', ordinatY, '-> 1')
# elif ordinatY>0 and abscisaX<0:
#     print('X= ', abscisaX, 'Y= ', ordinatY, '-> 2')
# elif ordinatY<0 and abscisaX<0:
#     print('X= ', abscisaX, 'Y= ', ordinatY, '-> 3')
# elif ordinatY<0 and abscisaX>0:
#     print('X= ', abscisaX, 'Y= ', ordinatY, '-> 4')
# elif ordinatY==0:
#     print('X= ', abscisaX, 'Y= ', ordinatY, '-> на оси X')
# else:
#     print('X= ', abscisaX, 'Y= ', ordinatY, '-> на оси Y')

# Задача 4
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

# numberQuater=int(input('Введите номер четверти на плоскости OXY (1,2,3,4) = '))
# if numberQuater==1:
#     print('X > 0 и Y > 0')
# elif numberQuater==2:
#     print('X < 0 и Y > 0')
# elif numberQuater==3:
#     print('X < 0 и Y < 0')
# elif numberQuater==4:
#     print('X > 0 и Y < 0')
# else:
#     print ('Неверный ввод номера четверти! Повторите ')

# Задача 5
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# print ('Введите координаты точки A на оси OXY')
# abscisA=float(input('Xa= '))
# ordinateA=float(input('Ya= '))
# print ('Введите координаты точки Bа оси OXY')
# abscisB=float(input('Xb= '))
# ordinateB=float(input('Yb= '))
# if abscisA==abscisB and ordinateA==ordinateB:
#     print('Координаты точек А и В совпадают')
# else:
#     lenthAB=sqrt((ordinateB-ordinateA)**2+(abscisA-abscisB)**2)
#     print('A (',abscisA,ordinateA,'); B (',abscisB,ordinateB,') ->', round(lenthAB,2))

# Seminar 4/09/2022--------------------------------------------------------------------------------------------------------------
# Задача 1
# Напишите программу, которая принимает на вход 5 чисел и вычисляет максимум

from operator import itemgetter, truediv
from tkinter import N


# i=1
# while i<=5:
#     number=input(f'Введите {i}-е число ') # делает красивый вывод
#     if i==1:
#         max=number
#     elif number>max:
#         max=number
#     i+=1
# print (f'max={max}')

# Задача 2
# Напишите программу, которая принимает на вход N и выводит числа от -N до N

# n=int(input('Введите значение N = '))
# outN=list(range(-n,n+1)) # +1 добавили т.к. range берет значения до последнего
# print(outN)

# Задача 3
# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа

# x=float(input('Введите дробное число х= '))
# y=x*10
# y=y%10
# print(int(y))

# --------------------------------------------------------------------------------------------------
# ЛЕКЦИЯ №2 Знакомство с python. Функции, данные и модули. 10.09.2022
# Работа с файлами
# color={'red', 'green', 'blue'}
# data=open('file.txt', 'w')
# data.writelines(color) #разделителей не будет
# data.write('\nLine')
# data.close()

# при наличии файла file.txt
# with open('file.txt','a') as data:
#     data.write('\nline123\n')
#     data.write('line213')

# считать данные из файла
# path = 'file.txt'
# data=open(path, 'r')
# for line in data:
#     print (line)
# data.close()

# считать script (код) из файла
# import hello
# print(hello.f(2.3))
# для упрощения, чтобы не писать везде название файла
# import hello as h # hello переименовали в h
# print (h.f(1))

# ФУНКЦИИ
# 1 вариант
# def new_string(symbol,count): # в функции символ и число
#     return symbol*count
# print (new_string('x',6)) # получаем xxxxxx

# # 2 вариант
# def new_string(symbol,count=3): # в функции символ и фиксированное число
#     return symbol*count
# print (new_string('x')) # можно не указывать второй аргумент-число т.к. оно задано
# print (new_string(4)) # в python распознается тип данных в момент выдачи поэтому вместо символа (symbol) 
# # можно задать и число и код сработает
# print (new_string('x', 7)) # можно изменить фиксированное число

# 3 вариант (неограниченные параметры)
# def constinatio (*params):
#     res: str='' #указывается тип данных, если будут указаны числа, то будет арифмет операция 
#     #(указывать тип не обязательно)
#     for item in params:
#         res+=item
#     return res
# print (constinatio('o','l','e','g'))

# ФУНКЦИИ - РЕКУРСИЯ на примере Фибоначи
# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# list=[]
# for e in range (1,20):
#     list.append(fib(e))
# print(list)

# КОРТЕЖИ - неизменяемые списки, похоже на массив, то есть перезаписать эл картежа нельзя
a=(3, 4, 5)
#  0, 1, 2
#  -3, -2, -1
print(a[0]) # 3
print(a[-1]) # 5 ( в python  вычисление элемента списка может быть справа налево)
print(a[2]) #5

b=(3,) # присваивание одному элементу в кортеже

#Словари
# dictinary={}
# dictinary=\
#     {
#         '1':'one',
#         '2':'two',
#         '3':'three'
#     }
# print (dictinary)
# print(dictinary['3'])

# c циклом keys and value в словаре нужен for
# for k in dictinary.keys():
#     print(k) # выводятся ключи

# for k in dictinary.values():
#     print(k) # выводяться значения 

# добавление и изменение значения в словаре
# dictinary['up']='true' # добавил новое значение
# dictinary['1']='new 1' # изменил значение c указанным ключем c 1 на new 1
# print(dictinary['1'])

# Множества
# Операции множества
# color={'red', 'blue', 'green'}
# print(color) #{'green', 'red', 'blue'}
# color.add('gray') #добавление
# print(color) #{'green', 'red', 'gray', 'blue'}
# color.remove('red') # удаление элемента (удалить несущ эл нельзя)
# print(color) # {'green', 'blue', 'gray'}
# color.clear() # очищение множества
# print(color) #set() нет элементов
# color.add('blue')
# print(color) #{'blue'}
# color.discard('blue') # еще одно удаление элемента множества
# print(color) #set() нет элементов

a={1,2,3,5,6,8,5}
b={1,2,5,8,15,78}
c=a.copy() # копирование множества
u=b.union(a) # объединение множеств
print(u) #{1, 2, 3, 5, 6, 8, 78, 15}
i=a.intersection(b) # пересечение множеств
print(i) #{8, 1, 2, 5} 
d1=a.difference(b) # пересечение
print(d1) #{3, 6}
d2=b.difference(a)
print(d2) #{78, 15}
q=a\
    .union(b)\
    .difference(a.intersection(b)) # множественные действия с множествами
print(q)

f=frozenset(a) # замораживает множество - его нельзя изменить
# ----------------------------------------------------------------------------
    