#!/usr/bin/python
#coding:utf8

l = list(range(13))
l1 = []
for i in range(13):
	d = i % (13 - i) #之前我在这里犯了一个错误，用 len(l) 去减 i，因为 l 在遍历过程中是变化的，所以导致出错。其实，这里 len(l) = 13 - i，所以直接用 len(l) 也可以。
	l = l[d:] + l[0:d]
	x = l.pop(0)
	l1.append(x)


print(l1)
l2 = [0] * 13#新建一个空列表，用来接收数据
l3 = list(range(1, 14))

k = 0
for i in l1:
	l2[i] = l3[k]
	k += 1

print(l2)
