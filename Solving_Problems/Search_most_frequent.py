#!/usr/bin/python
#coding:utf8

def search(s, k):
    '''这个函数可以搜索一个序列，从中找出出现频率最高的包含 k 个元素的子字符串。'''
    
    l0 = []
    for i in range(len(s) - k +1):
        t0 = s[i:i+k]
        l0.append(t0)

    l = []
    l1 = []
    for i in range(len(s) - k +1):
        t = s[i:i+k]
        if t not in l:
            l.append(t)
            l1.append(l0.count(t))#这里之所以要用列表统计是因为字符串的 count 函数统计的是非 overlapping 的情况，这样可能漏掉一些存在 overlapping 的情况。

    l3 = []
    while l1:
        m = max(l1)
        p = l1.index(m)
        l3.append((l[p], l1[p]))
        del l[p]
        del l1[p]

    for i in range(len(l3) - 1):
        if l3[i][1] > 1:
            print(l3[i])
            if l3[i][1] > l3[i+1][1]:
                break
    else:
        print('No substring of %d elements repeats more than one time.' % k)

