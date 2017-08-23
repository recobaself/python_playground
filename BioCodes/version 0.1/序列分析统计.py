#!/usr/bin/python
#coding:utf8

def mysort(x):
    "In this case, x shuld be a string, list or tuple only."
    s = list(x)
    s1 = s[::]
    l = []
    for i in range(len(s)):
        t = max(s1)
        l.append(t)
        s1.remove(t)
    return l

def mysort1(x):
    "In this case, x is a list that consists of tuples only. e.g. [('A', 2), ('B', 5), ('C', 3), ('D', 8), ('E', 6)]"
    l = []
    for each in x:
        l.append(each[1])
    l1 = []
    x1 = x[::]
    l2 = l[::]
    for i in range(len(l)):
        t = max(l2)
        for each in x1:
            if each[1] == t:
                l1.append(each)
                l2.remove(t)
                x1.remove(each)
                break
    return l1

def counter(s):
    "This script is used to analyze DNA or Protein sequence."
    l = list(s)
    l1 = [l[0]]
    l2 = [(l[0], l.count(l[0]), format((l.count(l[0]) / len(l)), '.2%'))]
    for i in l:
        if i not in l1:
            m = l.count(i)
            p = format((m / len(l)), '.2%')
            t = (i, m, p)
            l2.append(t)
            l1.append(i)
    print('剔除掉重复的元素以后得： ', l1)
    print('统计元素出现频率得： ', l2)
    result = mysort1(l2)
    print('排序后得： ', result)
    print('分行显示如下： ')
    i = 1
    for item in result:
        print(i, '.', item)
        i += 1

def process(x):
    "This script is used to process DNA or Protein sequence for counter function. 这个脚本用来去除DNA或者蛋白序列中的空格和换行符号。"
    x = x.upper()
    l = list(x)
    if '' in l:
        m = l.count('')
        for i in range(m):
            l.remove('')
    if ' ' in l:
        p = l.count(' ')
        for i in range(p):
            l.remove(' ')
    if '\n' in l:
        n = l.count('\n')
        for i in range(n):
            l.remove('\n')
    return l

def mostcommon(s, n):
    "This script is used for analyze the most common element in a sequence."
    l = list(s)
    l1 = [l[0]]
    l2 = [(l[0], l.count(l[0]), format((l.count(l[0]) / len(l)), '.2%'))]
    for i in l:
        if i not in l1:
            m = l.count(i)
            p = format((m / len(l)), '.2%')
            t = (i, m, p)
            l2.append(t)
            l1.append(i)
    result = mysort1(l2)
    for k in range(len(result)):
        if result[k][1] > result[k+1][1]:
            mc = result[:k+1]
            break
    if n == 1:
        for item in mc:
            print(1, '.', item)
    if n > 1:
        print('除去出现频率最高的元素，其余元素的出现频率依次为： ', result[k+1:])
        i = 2
        for item in result[k+1:]:
            print(i, '.', item)
            i += 1
