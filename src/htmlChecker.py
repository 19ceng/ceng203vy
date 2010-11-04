#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, sys
from stack import Stack

def parser(fnm):
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

	while i < len(tags) and balanced:
		tag = tags[i]
		
		if tag[0] != '/':
			s.push(tag)
		else:
			if s.isEmpty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top, tag):
					balanced = False

		i = i + 1

	if balanced and s.isEmpty():
		return True
	else:
		return False

def matches(open, close):
	return open == close[1:]

if __name__ == "__main__":
	print checker(parser('index1.htm'))
	print checker(parser('index2.htm'))
	print checker(parser('index3.htm'))
