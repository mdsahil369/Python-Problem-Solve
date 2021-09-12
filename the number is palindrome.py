user_input = '848752'

time_of = 10#hear 1 problem
for time in range(1,time_of+1):
	if len(user_input) == time:
		if user_input == user_input[::-1]:
			print(int(user_input))
		else:
			for i in range(int(user_input),100000000):#hear 1 problem
				v = str(i)
				a = int(v[::-1])
				if i == a:
					print(int(i))
					break