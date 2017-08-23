#!/usr/bin/python
#coding:utf8

import time

#i = 0
#while i < 5:
#    print i
#    i += 1
#    time.sleep(1)
#    if i == 3:
#        break
#else:
#    print 'this is else'

#print 'while and else are over'

for i in range(10):
    print i
    time.sleep(1)
    if i == 6:
        break
else:
    print 'this is else'

print 'for and else are over'
