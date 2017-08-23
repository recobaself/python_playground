#!/usr/bin/python
#coding:utf8

#这几行代码是从 Coursera 课程 Algorithms for DNA Sequencing 里学到的，很漂亮的方法。一个是利用字典来转换碱基，一行代码搞定了之前要进行四次判断才能搞定的事；二是 t = Complement[base] + t，直接得到反转后的序列，省去 reverse 一道工序。

def reverseComplement(s):
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t