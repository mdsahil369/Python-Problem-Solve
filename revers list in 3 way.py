li = [1,2,3,4,5]
r = len(li) 

#  part 1
rev = li[::-1]
print(rev)

# part 2
rev1 = []
for i in range(1,r+1):
	v = li.pop()
	rev1.append(v)
print(rev1)

# part 3
lis = [1,2,3,4,5]
a = []
if r%2 == 0 and r >= 1:
	for j in range(1,r+1):
		p = lis.pop()
		a.append(p)
else:
	for j in range(1,r+1):
		p = lis.pop()
		a.append(p)
print(a)
