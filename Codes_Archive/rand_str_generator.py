#!/usr/bin/python
#coding:utf8

import random
import os
import time

source = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
N = len(source) - 1
print "To generate a random sequence that contains number n of elements, please input an integer. If you want a random sequence with random number of elements, please input 0. "
print '-'*80
while True:
    n = raw_input("Your input is:  ")
    if not n.isdigit():
        print 'Please input an integer. :-)'
    elif int(n) < 0:
        print 'No minus, please. :-)'
    else:
        break
s0 = ''
s1 = ''
if int(n) == 0:
    p = random.randint(1,1000)
    l0 = []
    for i in range(0, p):
        x = random.randint(0, N)
        j = source[x]
        l0.append(j)
    s0 = ''.join(l0)
    print 'A random sequence contain %d elements has been generated below.'%int(p)
    print '-'*80
    print s0
elif int(n) > 0:
    l1 = []
    for i in range(0, int(n)):
        x = random.randint(0, N)
        k = source[x]
        l1.append(k)
    s1 = ''.join(l1)
    print "A sequence that contains %d elements has been generated below."%int(n)
    print '-'*80
    print s1
print '-'*80
print 'Do you want to save the sequence to file? (Y/N)'
while True:
    save = raw_input('Input here: ')
    if (save == 'Y' or save == 'y') and s0 != '':
        lead = 'Your random sequence contain %d elements is below.'%int(p)
        foo = open('./random_sequence.txt', 'a+')
        foo.write('\n'+lead+'\n'+s0+'\n'+'-'*80)
        foo.close()
        print 'Your file has been saved.'
        break
    elif (save == 'Y' or save == 'y') and s1 != '':
        lead = 'Your random sequence contain %d elements is below.'%int(n)
        foo = open('./random_sequence.txt', 'a+')
        foo.write('\n'+lead+'\n'+s1+'\n'+'-'*80)
        foo.close()
        print 'Your file has been saved.'
        break
    elif save == 'N' or save == 'n':
        print 'OK. Done.'
        break
    else:
        print 'Please input Y or N, please.'
print '-'*80
print 'Complete.'

        
