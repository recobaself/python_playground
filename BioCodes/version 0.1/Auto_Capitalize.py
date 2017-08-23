#!/usr/bin/python
#coding:utf8

seq_input = raw_input('Please input your sequence here:  ')
l = []
s = ''
for x in seq_input:
    X = x.capitalize()
    l.append(X)
s1 = s.join(l)

print s1
