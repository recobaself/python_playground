#!usr/bin/python
#coding:utf8

#mcd:max_common_divisor

def mcd(a, b):#a and b are natural numbers.
	if a == b:
		return a

	t = min(a, b)
	cd = [i for i in range(1, t+1) if a % i == 0 and b % i == 0]
	m = max(cd)
	return m