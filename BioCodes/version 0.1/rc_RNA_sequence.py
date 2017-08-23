#!/usr/bin/python
#coding:utf8
import re
import os
import time

while True:
    seq_input = raw_input('Please input your RNA sequence here:  ')
    i = 0
    for x in seq_input:
        if x in 'AUGCaugc':
            i += 1
        else:
            i += 0
    if i < len(seq_input):
        print 'Please check your sequence. Only A, U, G, C please.'
    elif i > len(seq_input):
        print 'Are you kidding?'
    else:
        break

Name = raw_input('Please name your sequence:  ')
l = []
s = ''
for x in seq_input:
    X = x.capitalize()
    l.append(X)
S = s.join(l)

l1 = []
for x in S:
    if x == 'A':
        y = 'T'
    elif x == 'U':
        y = 'A'
    elif x == 'G':
        y = 'C'
    elif x == 'C':
        y = 'G'
    l1.append(y)
S_c = ''.join(l1)

sc_seq_input = S_c[::-1]
print 'The reverse complement DNA sequence to your RNA %s is below.'%Name
print "5'-", sc_seq_input, " -3'"

Name1 = Name + '_'
Date = time.strftime('%Y_%m_%d',time.localtime(time.time()))
itemname = Name1 + Date
content = '\n' + itemname + ':' + "\n5'-" + sc_seq_input + " - 3'"
foo = open('./rc_RNA_to_DNA.txt', 'a+')
foo.write(content)
foo.close()
print 'A new item has been added in the rc_RNA_to_DNA.txt'
