#!/usr/bin/python
#coding:utf8

#Monte Carlo Method to calculate Pi

import random

while 1:

    print('Input a integer number here to calculate pi using Monte Carlo method.Input 0 to quit the program.')

    n = int(input('Please input your number here: '))
    
    if n == 0:
        break

    data = [(random.uniform(0,1), random.uniform(0,1)) for i in range(n)]

    in_c = [i for i in data if (i[0]**2 + i[1]**2) < 1]
    on_c = [i for i in data if (i[0]**2 + i[1]**2) == 1]
    out_c = [i for i in data if (i[0]**2 + i[1]**2) > 1]

    print('There are %d dots generated, %d of them are in the circle, %d of them are out of the circle, %d are on the circle.' % (n, len(in_c), len(out_c), len(on_c)))

    p = (len(in_c) + len(on_c)) / n

    print('The probility of dots that will be in the circle is %f' % p)

    print('When number n is %d, pi is roughly %f' % (n, p * 4))

