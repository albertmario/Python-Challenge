#!/usr/bin/env python

import Image

im = Image.open('../src/mozart.gif')
new = Image.new(im.mode, im.size)
p, l = im.size

def straight(row):
	i = 0
	while row[i] != 195:
		i += 1

	return row[i:] + row[:i]

for i in range(l):
	row = [im.getpixel((j, i)) for j in range(p)]
	row = straight(row)
	[new.putpixel((j,i), row[j]) for j in range(p)]

new.show()
