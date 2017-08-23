#!/usr/bin/python
#coding:utf8
import re
import time
import random

#Check sequence composition to preclude non-A/T/G/C elements.
while True:
    DNA_seq = raw_input('Please input your DNA sequence here:  ')
    print 'Checking your DNA sequence ...'
    time.sleep(1)    
    i = 0
    for x in DNA_seq:
        if x in 'aAtTgGcC':
            i += 1
        else:
            i += 0
    if i == len(DNA_seq):
        break
    elif i < len(DNA_seq):
        print 'Please input only A, T, G and C. '
    else:
        print 'i > len(DNA_seq), are you kidding?'
#Analyze the length of the sequence
while True:
    if len(DNA_seq) < 50:
        print 'Your sequence is shorter than 50 nt. Please check your input.'
        exit()
    elif len(DNA_seq) >= 50 and len(DNA_seq) < 100:
        print 'Your sequence is shorter than 100 nt. Are you sure to preceed?'
        while True:
            Confirmation = raw_input('Y or N:  ')
            if Confirmation == 'Y' or Confirmation == 'y':
                break
            elif Confirmation == 'N' or Confirmation == 'n':
                exit()
            else:
                print 'Please input Y or N.'
        break
    else:
        break
#Capitalize all the elements in the sequence
s = ''
l =[]
for i in DNA_seq:
    I = i.capitalize()
    l.append(I)
DNA_SEQ = s.join(l)
#Select primers
print 'The sequence you input is %d bp. Your primers are listed below.'%int(len(DNA_seq))
print '#'*80
time.sleep(1)
for n in range(18, 30):
    F_primer = DNA_SEQ[0:int(n)]
    m = int(n) + 1
    rc_R = DNA_SEQ[:-m:-1]
    l1 = []
    s1 = ''
    for i in rc_R:
        if i == 'A':
            j = 'T'
        elif i == 'T':
            j = 'A'
        elif i == 'G':
            j = 'C'
        elif i == 'C':
            j = 'G'
        l1.append(j)
    R_primer = s1.join(l1)
    F_GC = float((F_primer.count('G') + F_primer.count('C')))/len(F_primer)
    R_GC = float((R_primer.count('G') + R_primer.count('C')))/len(R_primer)
    print '%d nt primers are: '%int(n)
    print "Foward primer: 5'-", F_primer, "-3'", '    GC content: ', F_GC
    print "Reverse primer: 5'-", R_primer, "-3'", '    GC content: ', R_GC
    print '-'*80
print '#'*80
print 'Complete.'
