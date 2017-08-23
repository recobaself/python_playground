#!/usr/bin/python
#coding:utf8

#这个代码来自于 Coursera 课程 Algorithms for DNA Sequencing


def countATGC(s):
    '''
    这段代码简洁高效。如果用 s.count() 的方法的话，每计数一个碱基，其实都遍历了一次，不但效率比下面这段代码低，而且还显得代码冗长。
    '''
    counts = {'A' : 0, 'T' : 0, 'G' : 0, 'C' : 0}
    for base in s:
        counts[base] += 1

    return counts