#!/usr/bin/python
#coding:utf8
import os
import string
def touch(x):
    sfx = str(x)
    if '.txt' in sfx:
        name = './' + sfx
    else:
        name = './' + sfx + '.txt'
    foo = open(name, 'a+')
    foo.close

filename = raw_input('Please input the file name here:  ')
touch(filename)
