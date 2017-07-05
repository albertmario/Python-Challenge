#!/usr/bin/python

from PIL import Image

im = Image.open('cave.jpg')
l, t = im.size

odd = Image.new('RGB', (l, t))
even = Image.new('RGB', (l, t))

for i in range(t):
	for j in range(l):
		temp = im.getpixel((j, i))
		if (i + j) % 2:
			odd.putpixel((j, i), temp)
		else:
			even.putpixel((j, i), temp)

odd.show()
even.show()