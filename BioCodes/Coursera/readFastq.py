#!/usr/bin/python
#coding:utf8

#本代码来自 Coursera 课程 Algorithms for DNA Sequencing

def readFastq(filename):
	'''
	This function is to read a fastq file and get the sequence and quality info.
	The parameter here is a string of the name of the file to be read.
	A tuple will be returned.
	'''
	sequences = []
	qualities = []
	with open(filename) as fh:
		while True:
			fh.readline()
			seq = fh.readline().rstrip()
			fh.readline()
			qual = fh.readline().rstrip()
			if len(seq) == 0:
				break
			sequences.append(seq)
			qualities.append(qual)
	return sequences, qualities#因为返回的是一个元组，可以用两个变量将元组内的两个元素接收下来。就是所谓 multiple assignment

seqs, quals = readFastq('your filename')

def phred33ToQ(qual):
	'''
	This function is to convert the phred33 to Q score.
	'''
	return ord(qual) - 33

def createHist(qualities):
	'''
	这个函数统计了测序结果的可信度。 比如 Q score 达到 40 的有多少，20 的又有多少。
	'''
	hist = [0] * 50#这个列表是用来接收数据的，列表的每个元素的 index 代表了一个 Q score，元素的值表示这个 Q score 出现了多少次。
	for qual in qualities:
		for phred in qual:
			q = phred33ToQ(phred)
			hist[q] += 1
	return hist

h = createHist(quals)

import matplotlib.pyplot as plt

plt.bar(range(len(h)), h)
plt.show()

def findGCByPos(read):
	gc = [0] * 100
	totals = [0] * 100

	for read in reads:
		for i in range(len(read)):
			if read[i] == 'C' or read[i] == 'G':
				gc[i] += 1
			totals[i] += 1

	for i in range(len(gc)):
		if totals[i] > 0:
			gc[i] /= float(totals[i])

	return gc

gc = findGCBypos(seqs)
plt.plot(range(len(gc)), gc)
plt.show()

import collections

count = collections.Counter()
for seq in seqs:
	count.update(seq)
print(count)
