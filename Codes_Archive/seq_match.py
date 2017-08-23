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
q = 0
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

if q == 0:
    print 'There is no perfect match for your given pattern.'
if q > 0:
    print 'There are %d perfect matches across the target sequence. They are listed below in the format [([slice index], occurence ranking, matched sequence)].'%int(q)
    print '-'*80
    print l
    print 'Do you want to save the search result? (Y/N)'
    while True:
        sa = raw_input('Please input Y or N to confirm. Input here:  ')
        lead = '\n' + 'Alignment result on ' + time.strftime('%Y_%m_%d', time.localtime(time.time())) + ' is below.' + '\n' + '-'*80 + '\n'
        if sa == 'Y' or sa == 'y':
            foo = open('./alignment result.txt', 'a+')
            foo.write(lead + str(l) + '\n' + '-'*80)
            foo.close()
            print 'Done. Your result has been saved to alignment results.txt'
            break
        elif sa == 'N' or sa == 'n':
            print 'OK. The result will not be saved to file.'
            break
        else:
            print "Please input Y or N to proceed."
print '#'*80
print 'Complete.'
