#!/usr/bin/python

from PIL import Image

im = Image.open('wire.png')
im_new = Image.new('RGB', (100, 100), "white")

arah = [[1, 0], [0, 1], [-1, 0], [0, -1]]

a = -1
b = 0
c = 0

for i in range(250):
	skrng = arah[i % 4]
	bantu = (i + 1) // 2
	print bantu

	for j in range(100 - bantu):
		a += skrng[0]
		b += skrng[1]
		pix = im.getpixel((c, 0))
		im_new.putpixel((a, b), pix)
		c += 1

im_new.show()
