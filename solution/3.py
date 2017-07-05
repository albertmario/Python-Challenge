#!/usr/bin/python

import re

a = open('3.txt').read()

b = re.findall(r'[a-z]+[A-Z]{3}([a-z])[A-Z]{3}[a-z]+', a)
print "".join(b)
