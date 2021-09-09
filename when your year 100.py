# def discount(a,b):
#     return a - int((a*b)/100)

# print(discount(1000,50))

# import math

# def radians_to_degrees(rad):
# 	return round(math.degrees(rad),1)

# print(math)
while True: 
	try:
		age = int(input('What is your age or yera of barth : '))
		break
	except:
		print('invalid value')


def after_100(a):
	return (2021 - a) + 100
if age != 0:
	len_of_age = len(str(age))
	if len_of_age == 1 or len_of_age == 2 or len_of_age == 3:
		print(f'{after_100(age)} This year your age is 100')
		while True: 
			try:
				year = int(input('type a year when your year : '))
				break
			except:
				print('invalid value')
		if year != 0:
			if len(str(year)) == 4:
				print(year - (2021 - age)) 
			else:
				print('your age is invalide')
		else:
			print('your age is invalide')
	elif len_of_age == 4:
		age = 2021 - age
		print(f'{after_100(age)} This year your age is 100')
		while True: 
			try:
				year = int(input('type a year when your year : '))
				break
			except:
				print('invalid value')
		
		if year != 0:
			if len(str(year)) == 4:
				print(year - (2021 - age)) 
			else:
				print('your age is invalide')
		else:
			print('your age is invalide')
	else:
		print('your age is invalide')
else:
	print('your age is invalide')




















