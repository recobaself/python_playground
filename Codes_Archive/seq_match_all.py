#!/usr/bin/python
#coding:utf8

import time
import os
import re

target = raw_input('Please input your sequence to be analyzed here:  ')
N = int(len(target))
print 'Your sequence to be analyze contains %d elements.'%int(N)
prey = raw_input('Please input your given pattern sequence here:  ')
M = int(len(prey))

l = []
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
q = 0
q1 = 0
q2 = 0
q3 = 0
q4 = 0
q5 = 0
for i in range(0, N-M+1):
    k = 0
    for j in range(0, M):
        if target[i+j] == prey[j]:
            k += 1
    if k == M:
        q += 1     
        t = ([i, i+M], q, prey)
        print t
        l.append(t)
    elif k == M - 1 and k > 0:
        q1 += 1
        t1 = ([i, i+M], q1, 'one mismatch')
        print t1
        l1.append(t1)
    elif k == M - 2 and k > 0:
        q2 += 1
        t2 = ([i, i+M], q2, 'two mismatches')
        print t2
        l2.append(t2)
    elif k == M - 3 and k > 0:
        q3 += 1
        t3 = ([i, i+M], q3, 'three mismatches')
        print t3
        l3.append(t3)
    elif k == M - 4 and k > 0:
        q4 += 1
        t4 = ([i, i+M], q4, 'four mismatches')
        print t4
        l4.append(t4)
    elif k == M - 5 and k > 0:
        q5 += 1
        t5 = ([i, i+M], q5, 'five mismatches')
        print t5
        l5.append(t5)
    else:
        print 'pass'

if q == 0:
    print 'There is no perfect match.'
if q > 0:
    print 'The perfect matches across the whole sequenc occure %d times. And they are listed below.'%int(q)
    print l
if q1 > 0:
    print 'One-mismatches occur %d times. And they are listed below.'%int(q1)
    print l1
if q2 > 0:
    print 'Two-mismatches occur %d times. And they are listed below.'%int(q2)
    print l2
if q3 > 0:
    print 'Three-mismatches occur %d times. And they are listed below.'%int(q3)
    print l3
