#!/usr/bin/python

from PIL import Image

im = Image.open('oxygen.png')
l, t = im.size

hasil = ''

for i in range(0, l, 7):
	hasil += chr(im.getpixel((i, t / 2 ))[0])

print hasil