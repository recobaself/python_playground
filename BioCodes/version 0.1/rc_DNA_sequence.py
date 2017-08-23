#!/usr/bin/python
#coding:utf8

#初学时写的代码，再看时觉得好繁琐啊，:-)

import time
print 'Please follow the instruction to input your primer. Only A,T,G or C, no numbers. :-)'
print "*"*80
while True:
    seq_input = raw_input('Please input your primer sequence here:  ')
    print 'Analyzing your sequence, please wait a second, :-)'
    time.sleep(1)
    i = 0
    for x in seq_input:
        if x in 'AaTtGgCc':#这里完全可以写成 if x not in 'ATGCatgc'
            i+=1
        else:
            i+=0
    if i == len(seq_input):
        break
    elif i < len(seq_input):
        print 'only capitalized A, T, G, or C please. )'

print 'Let me get the complement sequence first. :-p'

l = []
s = ''
for x in seq_input:#这里完全可以用 string.upper()方法
    X = x.capitalize()
    l.append(X)
s1 = s.join(l)

l1 = []

for z in s1:
    if z == 'A':
        z1 = z.replace('A', 'T')#直接 z1 = 'T' 不就得了嘛
    elif z == 'T':
        z1 = z.replace('T', 'A')
    elif z == 'G':
        z1 = z.replace('G', 'C')
    elif z == 'C':
        z1 = z.replace('C', 'G')
    l1.append(z1)
s2 = s.join(l1)

print 'Below is the complement sequence.'
print s2

print 'Let\'s reverse the sequence to get it in 5\' to 3\' direction.'
print s2[::-1]


