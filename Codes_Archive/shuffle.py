#!/usr/bin/python
#coding:utf8

import random

def shuffle(list):
	n = len(list) - 1
	l = []
	for i in range(n, -1, -1):
		k = random.randint(0, i)
		l.append(list[k])
		del list[k]
		print(list)
	return l

list = range(1, 20)

shuffle(list)

