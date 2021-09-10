# 10 apple mn=2,mx=4--->2 is divisor of 10,3 isn't divisor of 10,4 is divisor of 10.
# 1.get input
# 2.processing
# 3.and give output

amound_of_apple = int(input('Which amound of apple avelable in harry : '))
min_number = int(input('min number : '))
max_number = int(input('max number : '))

if min_number != max_number :
	for i in range(min_number,max_number+1):
		if amound_of_apple%i == 0:
			print(f'{i} is divison of {amound_of_apple} And each people get {amound_of_apple/i} Apple')
		else:
			print(f'{i} is\'nt divison of {amound_of_apple}')
