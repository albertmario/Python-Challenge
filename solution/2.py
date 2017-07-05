#!/usr/bin/python

import string

a = open('2.txt').read()
hasil = ''

for i in a:
	if i in string.ascii_lowercase or i in string.ascii_uppercase:
		hasil += i

print hasil