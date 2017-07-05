#!/usr/bin/python

a = open('evil2.gfx', 'rb').read()
# open('1.jpg', 'wb').write(a[1::5])
for i in range(5):
	open(str(i)+'.jpg', 'wb').write(a[i::5])