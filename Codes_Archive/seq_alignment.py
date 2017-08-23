#!/usr/bin/python
#coding:utf8

import os
import time
import re

def align2(sp, st):
    if len(sp) != len(st):
        return 'The align2 function is not availabe to two sequences with different length.'
    else:
        N = len(sp)
        k = 0
        l = []
        for i in range(len(sp)):
            if sp[i] == st[i]:
                k += 1
                l.append(i)
            else:
                k += 0
        r = float(k)/N
        return r, k, N, l

#This is a module.

