#!/usr/bin/python
#coding:utf8

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
	
def searchfast(a, b):
    if a not in b:
	    return 'No perfect match. Search stopped.'
	else:
	    matched_collection = []
		for i in range(len(b) - len(a) + 1):
		    if b[i] == a[0] and b[i+1] == a[1]:
			    for j in range(2, len(a)):
				    if a[j] != b[i+j]:
					    break
				else:
				    matched = (i+1, i+j+1)
					matched_collection.append(matched)
		return matched_collection

def searchdeep(a, b):
    'a is a part of b. This function is to find a in b.'
    matched_collection = []
    similar_collection = []
    for i in range(len(b) - len(a) + 1):
        score = 0
        for j in range(len(a)):
            if a[j] == b[i+j]:
                score += 1
            else:
                score += 0
        if score == len(a):
            matched = (i+1, i+j+1)
            matched_collection.append(matched)
        if 0.5 < float(score)/len(a) < 1:
            similar = ((i+1, i+j+1), format((float(score)/len(a)), '.2%'))
            similar_collection.append(similar)
    if matched_collection and similar_collection:
        sorted_similar_collection = mysort1(similar_collection)
        print 'The perfectly matched regions are: ', matched_collection, '\n', 'Regions that have high similarity are: ', sorted_similar_collection
    elif matched_collection:
        print 'The perfectly matched regions are: ', matched_collection
    elif similar_collection:
        sorted_similar_collection = mysort1(similar_collection)
        print 'Regions that have high similarity are: ', sorted_similar_collection
    else:
        print 'Search failed. No high similarity found.'

