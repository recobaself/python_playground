#!/usr/bin/python
#coding:utf8

l = []
for n in range(2, 1000):
    for x in range(2, n):
        if n % x == 0:
            print n, 'euqals', x, '*', n/x
            break
    else:
        l.append(n)
        print n, 'is a prime number.'
print l
