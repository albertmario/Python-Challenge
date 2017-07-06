#!/usr/bin/python

import calendar

for i in range(1000, 2000):
	if calendar.isleap(i):
		c = calendar.monthcalendar(i, 1)

		if c[0][3] == 1 and i % 10 == 6:
			print i