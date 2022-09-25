def inp_num(type_num): 
	'''Функция возвращает либо целое, либо вещественное введенное число. Проверяет правильность ввода.
	При вх 1 - проверяет, что введенное число целое.
	При вх 0 - проверяет, что введенное число вещественное, а не буквы или знаки.'''
	ind=0
	while ind==0:
		num=input('n=')
		if type_num==1: #целое
			if num.isnumeric()==1:
				return int(num)
		count_dig_num=0
		if type_num==0:
			for i in num: #вещественное
				if i.isnumeric()==1 or '.'==i or '-'==i:
					count_dig_num=count_dig_num+1
			if count_dig_num==len(num):
				return float(num)
		print('повторите ввод')

def input_list(type): 
	'''Функция возвращает список из целых или вещественных чисел. При вх параметре 0 -целые, при 1 - вещественные. Иначе выдает "Повторный ввод".
	Входной параметр задается на этапе написания программы.'''
	print('Введите количество элементов списка')
	len_list=inp_num(1)
	num_list=[]
	for ind_list in range(len_list):
		print(f'Введите {ind_list+1}-й эл списка')
		el_list=inp_num(type)
		num_list.append(el_list)
	print(f'Ваш список{num_list}')
	return num_list

def num_frac (num):
	'''
	Функция находит дробную часть от вещественного числа до 2 знаков
	'''
	frac=num-int(num)
	return round(frac,2)


def min_max_list(list,param): 
	'''
	Функция определяет в списке (первый входной параметр функции) максимум и минимум.
	При значении второго параметра 0 - возращает минимум.
	При значении второго параметра 1 - возращает максимум.
	'''
	min_l=min(list)
	max_l=max(list)
	if param==0:
		return min_l
	elif param==1: 
		return max_l
	else: print('Ошибка второго параметра или 0 или 1')

def revers_list(list_in):
	'''Функция возвращает обратный список входному.  
	Пример вх: [1,1,2,3,5] - > вых [5,3,2,1,1]'''
	list_out=[]
	for ind in range(len(list_in)-1,-1,-1):
		list_out.append(list_in[ind])
	return list_out

