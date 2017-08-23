#!/usr/bin/python
#coding:utf8

import time
import os

class DNA():
    def __init__(self, seq):
        self.seq = seq
        seq_l = list(self.seq.upper())
        seq_l1 = seq_l[::]
        if ' ' in seq_l or '\n' in seq_l:
            print('您输入的序列中含有空格或换行符等不相关字符，正在为您剔除不相关字符...')
            time.sleep(2)
            for item in seq_l:
                if item == ' ' or item == '\n':
                    seq_l1.remove(item)
        self.seq = ''.join(seq_l1)
        print('您输入的序列为: ', self.seq)
        for item in self.seq:
            if item not in 'ATGC':
                print('您输入的序列中含有除ATGC之外的字符，请检查您的序列！')
                break
