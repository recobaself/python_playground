#!/usr/bin/python
#coding:utf8

#定义一个函数，在已有质数列表基础上寻找下一个质数

def nextprime(l):
	""" 
	This function is to generate the next prime number based on the prime number list that provided.
	Thus, l argument should be a prime number list.  
	nextprime(l) --> list
	"""
	k = max(l) + 1

	while True:
		
		FoundDivisor = False

		for prime in l:
			if k % prime == 0:
				FoundDivisor = True
				break
		if FoundDivisor:
			k += 1
		else:
			print("A new prime number %d has been found." % k)
			l.append(k)#注意：曾经在这里犯错，写成 l = l.append(k) 简直是多此一举弄成拙
			return l

#给出给定范围内所有质数的列表的方法 1

def findprime(x):
	"""
	This function generate a list containing all the prime numbers less than x.
	It takes advantage of nested for loop to find prime numbers.
	x argument should be a natural number that is more than two.
	findprime(x) --> list
	"""
	temp_list = range(2, x)
	prime_list = []

	for i in temp_list:
		for j in range(2, i):
			if i % j == 0:
				break
		else:
			prime_list.append(i)

	return prime_list

n = int(input("Please input a natural number: ")) #n should be a natural number, which means it is a positive integer. n also should be more than 1.
prime_list = findprime(n)
print(prime_list)

#给出给定范围内所有质数的列表的方法 2

def findprime2(x):
	"""
	This is another method to generate a prime number list.
	It takes advantage of the filter method of list.
	x argument should be a natural number greater than two.
	findprime2(x) --> list
	"""
	init_list = list(range(2, x))

	for i in range(2, x):
		init_list = list(filter(lambda x : x == i or x % i, init_list))#这里完全可以用一个列表推导式来实现。

	return list(init_list)
