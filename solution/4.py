#!/usr/bin/python

import requests

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
r = requests.get(url+'12345')

while 1:
	print r.text
	hasil = r.text.split()[-1]
	r = requests.get(url+hasil)