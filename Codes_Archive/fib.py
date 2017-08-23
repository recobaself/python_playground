#!/usr/bin/python
#coding:utf8

import os
import time
import re

def fib(a, b, n):
    i=0
    l=[]
    while i<=n:
        l.append(a)
        a,b=b,a+b
        i+=1
    else:
        print 'while loop end after %d cycles. Your sequence generated below.'%n
    return l

fibseq = fib(0,1,20)
print fibseq


