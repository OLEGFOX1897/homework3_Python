# Задача 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# 0.56 -> 11

# number=float(input('Введите вещественное число N='))
# if number<0:
#     number=number*(-1)
#     signNum=-1
# else:
#     signNum=1 
#     strNumber=str(number)
# sumDigit=0
# for ind in list(strNumber):
#     if ind!='.':
#         sumDigit=sumDigit+int(ind)
# print(f'{number*signNum} -> {sumDigit}')

# Задача 2 Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# ind=1
# factorial=1
# while ind>0:
#     strNumber=input('Введите целое положительное число N=')
#     for i in list(strNumber):
#         if i=='.' or strNumber.isnumeric()==0:
#             ind=1
#         else:
#             ind=0
#     if ind>0:
#         print('Проверьте введеное значение')
# for ind in range(1,int(strNumber)+1):
#     factorial=ind*factorial
#     list.append(factorial)
# print(f'{strNumber}->{list}')

# # Задача 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

# ind=0
# while ind==0:
# 	num=int(input('Введите целое положительное чило N = '))
# 	if num<0:
# 		print('Повторите ввод')
# 	else:
# 		ind=1
# def num2(num):
# 	num2=0
# 	listNum=list(str(num))
# 	lenListNum=len(listNum)
# 	for i in range(0,lenListNum):
# 		num2=num2+10**(lenListNum-1-i)*int(listNum[lenListNum-1-i])
# 	return num2
# num1=num
# i=0
# while i==0:
# 	if num1==num2(num1):
# 		print(f'Полиндром числа {num} -> {num1}')
# 		i=1
# 	else:
# 		num1=num1+num2(num1)
# 		i=0


# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)
# данное решение было предложено на очередном семинаре
# но мной было разобрано т.к. в исходной версии у меня не запустилось

import datetime, math
def ranDigit(min, max):
    d=max-min
    ms=datetime.datetime.now().microsecond/(10**6)
    rand_digit=math.ceil(d*ms)
    return min+rand_digit
print(ranDigit(-100,100)) 
