#!/usr/bin/python

b = '1'

for j in range(0, 30):
	temp = None
	count = 0
	hasil = ''

	for i in b:
		if temp == None:
			temp = i
			count = 1
		else:
			if i == temp:
				count += 1
			else:
				hasil += str(count) + temp
				temp = i
				count = 1

	hasil += str(count) + temp
	b = hasil

print len(b)