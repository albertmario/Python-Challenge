#!/usr/bin/python

import xmlrpclib

s = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
# print s.system.methodHelp('phone')
print s.phone('Bert')