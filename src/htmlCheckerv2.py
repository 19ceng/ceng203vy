#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, sys
from stack import Stack

def parser(fnm):
	print "# %s dosyasi isleniyor..." % (fnm)
	data = open(fnm).read()
	liste = re.findall(r'<[/]*\w+[^>]*>', data)
	liste = [i for i in liste if i[-2]!='/']	# <br /> benzerlerini ele
	# "<" ve ">" karakterlerini ele
	liste = [str.replace("<", "") for str in liste] 
	liste = [str.replace(">", "") for str in liste]
	# "a href=bla bla" -> "a"
	tags = [str.split(" ")[0] for str in liste]

	return tags

def checker(tags):
	s = Stack()

	balanced = True
	i = 0

	while i < len(tags):
		tag = tags[i]
		
		if tag[0] != '/':
			s.push(tag)
			print "I: [%s] tagi acildi" % (tag)
		else:
			if s.isEmpty():
				balanced = False
				print "E: [%s] acilmamis" % (tag)
			else:
				top = s.peek()
				if not matches(top, tag):
					balanced = False
					print "E: [%s] nin kapatmasi beklenirken [%s] geldi" % (top, tag)
				else:
					top = s.pop()
					print "I: [%s] tagi kapandi" % (tag)

		i = i + 1

	if balanced and s.isEmpty():
		print "HTML dengeli"
	else:
		if balanced:
			while s.isEmpty():
				print "[%s] kapatilmamis" % (s.pop())
		print "HTML dengesiz"

def matches(open, close):
	return open == close[1:]

if __name__ == "__main__":
	checker(parser('index1.htm'))
	checker(parser('index2.htm'))
	checker(parser('index3.htm'))
	checker(parser('index4.htm'))
