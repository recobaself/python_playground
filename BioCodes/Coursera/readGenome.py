#!/usr/bin/python
#coding:utf8

#本代码来自于 Coursera 课程 Algorithms for DNA Sequencing

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.strip()
    return genome