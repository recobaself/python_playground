#!/usr/bin/python
#coding:utf8
import random

print 'Please input an integer. The system will generate a sequece of random  numbers. The number of random numbers equals the integer you input. If you input 0, a sequence of random numbers of random number will be generated. In this case, random number range from 1 to 999.'
print '-'*100
while True:
    n = raw_input('Please input an integer here:  ')
    if not n.isdigit():
        print 'Please input an integer, :-)'
    elif int(n)<0 or int(n)>999:
        print 'Please input an interger between 0 and 999, :-)'
    elif int(n) == 0:
        p = random.randint(1,999)
        seq = []
        for i in range(0,p):
            seq.append(random.randint(1,999))
        print 'A list that contains %d random numbers is generated below.'%int(p)
        print  seq
        print '-'*100
        print 'The End'
        break    
    else:
        seq = []
        for i in range(0,int(n)):
            seq.append(random.randint(1,999))
        print 'The list that contains %d random numbers is below.'%int(n)
        print seq
        print '-'*100
        print 'The End'
        break
