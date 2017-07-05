#!/usr/bin/python

import string

a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

hasil = ''
for i in a:
	if i in string.ascii_lowercase:
		temp = ord(i) + 2
		if temp > 122:
			hasil += chr(96 + (temp - 122))
		else:
			hasil += chr(temp)
	else:
		hasil += i

print hasil