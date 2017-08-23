#!/usr/bin/python
#coding:utf8
import time
print 'Please follow the instruction to input your primer. Only A,T,G or C, no numbers. :-)'
print "*"*80
while True:
    seq_input = raw_input('Please input your primer sequence here:  ')
    print 'Analyzing your sequence, please wait a second, :-)'
    time.sleep(1)
    i = 0
    for x in seq_input:
        if x in 'ATGC':
            i+=1
        else:
            i+=0
    if i == len(seq_input):
        break
    elif i < len(seq_input):
        print 'only capitalized A, T, G, or C please. )'

print 'Let me get the complement sequence first. :-p'


if seq_input.count('A') == len(seq_input):
    c_seq_input = seq_input.replace('A', 'T')
elif seq_input.count('T') == len(seq_input):
    c_seq_input = seq_input.replace('T', 'A')
elif seq_input.count('G') == len(seq_input):
    c_seq_input = seq_input.replace('G', 'C')
elif seq_input.count('C') == len(seq_input):
    c_seq_input = seq_input.replace('C', 'G')
elif seq_input.count('A') == 0:
    seq_input_G = seq_input.replace('G', '3')
    c_seq_input_T = seq_input_G.replace('T', 'A')
    c_seq_input_C = c_seq_input_T.replace('C', 'G')
    c_seq_input = c_seq_input_C.replace('3', 'C')    
elif seq_input.count('T') == 0:
    seq_input_G = seq_input.replace('G', '3')
    c_seq_input_A = seq_input_G.replace('A', 'T')
    c_seq_input_C = c_seq_input_A.replace('C', 'G')
    c_seq_input = c_input_C.replace('3','C')
elif seq_input.count('G') == 0:
    seq_input_A = seq_input.replace('A', '1')
    c_seq_input_C = seq_input_A.replace('C', 'G')
    c_seq_input_T = c_seq_input_C.replace('T', 'A')
    c_seq_input = c_seq_input_T.replace('1', 'T')
elif seq_input.count('C') == 0:
    seq_input_A = seq_input.replace('A', '1')
    c_seq_input_G = seq_input_A.replace('G', 'C')
    c_seq_input_T = c_seq_input_G.replace('T', 'A')
    c_seq_input = c_seq_input_T.replace('1', 'T')
elif seq_input.count('A') == 0 and seq_input.count('T') == 0:
    c_seq_input_G = seq_input.replace('G', '3')
    c_seq_input_C = seq_input_G.replace('C', 'G')
    c_seq_input = c_seq_input_C.replace('3', 'C')
elif seq_input.count('A') == 0 and seq_input.count('G') == 0:
    c_seq_input_T = seq_input.replace('T', 'A')
    c_seq_input = c_seq_input_T.replace('C', 'G')
elif seq_input.count('A') == 0 and seq_input.count('C') == 0:
    c_seq_input_T = seq_input.replace('T', 'A')
    c_seq_input = c_seq_input_T.replace('G', 'C')
elif seq_input.count('T') == 0 and seq_input.count('G') == 0:
    c_seq_input_A = seq_input.replace('A', 'T')
    c_seq_input = c_seq_input_A('C', 'G')
elif seq_input.count('T') == 0 and seq_input.count('C') == 0:
    c_seq_input_G = seq_input.replace('G', 'C')
    c_seq_input = c_seq_input_G.replace('A', 'T')
elif seq_input.count('G') == 0 and seq_input.count('C') == 0:
    c_seq_input_A = seq_iput.replace('A', '1')
    c_seq_input_T = c_seq_input_A.replace('T', 'A')
    c_seq_input = c_seq_input_T.replace('1', 'T')
else:
    seq_input_A = seq_input.replace('A', '1')
    seq_input_G = seq_input_A.replace('G', '3')
    c_seq_input_C = seq_input_G.replace('C', 'G')
    c_seq_input_G = c_seq_input_C.replace('3', 'C')
    c_seq_input_T = c_seq_input_G.replace('T', 'A')
    c_seq_input = c_seq_input_T.replace('1', 'T')

print 'The complement sequence is  ', c_seq_input

print "Let me reverse the sequence to get it in  5' to 3' direction."
print 'Here is the reverse complement sequence of your primer:  ', c_seq_input[::-1]
print '*'*80
print 'Complete.'
