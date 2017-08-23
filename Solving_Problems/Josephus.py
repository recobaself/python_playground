#!/usr/bin/python
#coding:utf8

#利用filter()函数剔除当前列表中满足条件的所有元素，重组列表，再逐步进行
def jo(x):
    l1 = [i for i in x if x.index(i) % 3 == 2]
    l2 = [i for i in x if x.index(i) % 3 != 2]
    return l1, l2

def jose(x):
    l = []
    while len(x) > 2:
        if len(x) % 3 == 0:
            t1, t2 = jo(x)
            l.append(t1)
            x = t2
        elif len(x) % 3 == 1:
            t1, t2 = jo(x)
            l.append(t1)
            x = x[-1:] + t2[:-1]
        elif len(x) % 3 == 2:
            t1, t2 = jo(x)
            l.append(t1)
            x = x[-2:] + t2[:-2]
    return l, x

#每次剔除一个元素，重组列表，用 while 循环处理
def joseph(x):
    l = []
    while len(x) > 3:
        l.append(x[2])
        x = x[3:] + x[:2]
    l.append(x[2])
    x = x[:2]
    return l, x

#每次剔除一个元素，重组列表，用递归处理
def josephus(x, result=None):
    if result is None:
        result = []

    if len(x) > 3:
        result.append(x[2])
        x = x[3:] + x[:2]
        josephus(x, result)

    elif len(x) == 3:
        result.append(x[2])
        x = x[:2]
        result.extend(x)

    return result
