#!/usr/bin/python

import zipfile

file = zipfile.ZipFile('./channel/channel.zip', 'r')
path = './channel/'
dict_ = {}

for i in file.infolist():
	dict_[i.filename.split('.')[0]] = i.comment

hasil = dict_['90052']

a = open(path+'90052.txt').read().split()[-1]

while 1:
	try:
		hasil += dict_[a]
	except:
		break
		
	a = open(path+a+'.txt').read().split()[-1]

print hasil