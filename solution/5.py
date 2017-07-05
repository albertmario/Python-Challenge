#!/usr/bin/python3

import pickle

a = pickle.load(open('banner.p','rb'))
print(a)
for i in a:
	for j in i:
		print(j[0]*j[1], end='')
	print(end='\n')