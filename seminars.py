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
# print (f'X\tY\tZ\tresult')
# list=[0,1]
# for x in list:
#     for y in list:
#         for z in list:
#             print(f'{x}\t{y}\t{z}\t{not (x or y or z)==(not x and not y and not z)}')


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