#!/usr/bin/python
#coding:utf8



def yang(n):
	if n == 1:
		list = [1, 1]
		return list
	if n == 2:
		list = [1, 2, 1]
		return list
	if n == 3:
		list = [1, 3, 3, 1]
		return list
	if n > 3 & n % 2 == 0:
		l = [1, n]
		l1 = yang(n-1)
		for i in range(2, int(n/2 +1)):
			l.append(l1[i-1] + l1[i])
		list = l + l[-2::-1]
		return list
	if n > 3 & n % 2:
		l = [1, n]
		l1 = yang(n-1)
		for i in range(2, int((n+1)/2)):
			l.append(l1[i-1] + l1[i])
		list = l + l[::-1]
		return list

for i in range(1, 21):
        print('row #', i, ',', 'length =', len(yang(i)), ',', yang(i))

