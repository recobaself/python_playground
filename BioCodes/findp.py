#!/usr/bin/python
#coding:utf8

# This is a collection of means for searching a pattern through context.

def naive(p, t):
    '''
    This is the naive way to search pattern in text.
    '''
    if len(p) >= len(t):
        return 'Pleae input pattern first.'
    if not p in t:
        return 'No pattern p found in text. Done.'
    matched = {"counts":0, "positions":[]}
    for i in range(len(t) - len(p) + 1):
        for k in range(len(p)):
            if t[i+k] != p[k]:
                break
        else:
            matched["counts"] += 1
            matched["positions"].append((i, i+len(p)))
    return matched

def bad_char_rule(p, t):
    '''
    This is implementation of bad character rules of Boyer-Moore algorithm.
    In this case, len(p) = len(t). This function will return the stride value which p should move.
    (1, 1) means p exactly match t, and p should move 1 step to right.
    (0, 1) means p does not match t exactly, and p should move 1 step to right.
    (0, m) means p does not match t exactly, and p should move m step to right.
    To be noted that no bad character rules table is applied in this case. Therefore, everytime Python need to loop the p sequence to get the value to shift.
    To improve the efficiency, one should generate a bad character rules table to avoid loop every time.
    '''
    k = 0
    while -1 - k >= -len(p):#This while loop generate k, which represent where the first mismatch occurs from the right to left.
        if p[-1 - k] == t[-1 - k]:
            k += 1
        else:
            break
    if k == len(p):
        return (1, 1)
    if k == len(p) - 1:
        return (0, 1)
    if k < len(p) - 1:
        m = 0
        while -1 - k - m >= -len(p):
            if p[-1 - k - m] != t[-1 - k]:
                m += 1
            else:
                break
        return (0, m)

def bcr_table(p):
    '''
    This function generate a table of values for shift when bad character rule is applied.
    This table will help Python avoid loop to find shift value. Loop once, productivity leap.
    This talbe only for DNA sequence, which means only 'A', 'T', 'G', 'C' in p and t.
    '''
    bcr_table = {}
    k = 1
    while k <= len(p):#k is the first mismatch from right to left.
        bcr_table[-k] = {}
        
        for i in range(-k - 1, -len(p) - 1, -1):
            if p[i] == 'A':
                bcr_table[-k]['A'] = -k - i
                break
        else:
            bcr_table[-k]['A'] = len(p) - k + 1
        
        for i in range(-k - 1, -len(p) - 1, -1):
            if p[i] == 'T':
                bcr_table[-k]['T'] = -k - i
                break
        else:
            bcr_table[-k]['T'] = len(p) - k + 1
        
        for i in range(-k -1, -len(p) - 1, -1):
            if p[i] == 'G':
                bcr_table[-k]['G'] = -k - i
                break
        else:
            bcr_table[-k]['G'] = len(p) - k + 1
        
        for i in range(-k - 1, -len(p) - 1, -1):
            if p[i] == 'C':
                bcr_table[-k]['C'] = -k - i
                break
        else:
            bcr_table[-k]['C'] = len(p) - k + 1
        
        k += 1

    return bcr_table

def bcr_table1(p):
    '''
    This is another version to get the bad character rules table for pattern p.
    '''
    bcr_table = {}
    for i in range(-1, -len(p), -1):#i is the first mismatch from right to left.
        bcr_table[i] = {}
        t = p[i-1::-1]

        for item in 'ATGC':
            if item in t:
                bcr_table[i][item] = t.find(item) + 1#我原先的思路是用 while 循环遍历找到该 item 的下标
            else:
                bcr_table[i][item] = len(t) + 1
    bcr_table[-len(p)] = {'A':1, 'T':1, 'G':1, 'C':1}

    return bcr_table

def bad_char_rule1(p, t, b_table):
    '''
    This version of bad character rule function takes advantage of bad character rule talbe to improve efficiency.
    p is the pattern, t is a slice of text that equals p in length.
    To call this function, the user should call bcr_table or bcr_table1 function to get the bad character rule table and use it as a parameter for this function.
    '''

    k = 0
    while -1 - k >= -len(p):#inner loop to determin k
        if p[-1 - k] == t[-1 - k]:
            k += 1
        else:
            break
    if k == len(p):
        return 1, 1
    else:
        return 0, b_table[-1-k][t[-1-k]]


def gsr_table(p):
    '''
    This function create a good suffix rule table for the give pattern. 
    Using this table to search patter p in text should increase efficiency.
    '''
    gsr_table = {}
    for i in range(-2, -len(p)-1, -1):#i is the first mismatch from right to left. i can not be -1, otherwise the good suffix rule fail.
        gsr_table[i] = {}
        temp = p[i+1:]#temp is the matched region befor i from right to left.
        collection = []#This is to collect the substrings that equal with temp.
        for m in range(len(p[:-1]) - len(temp) +1):#See above. Here use len(p[:-1]) is to exclude temp itself.
            for k in range(len(temp)):
                if p[m+k] != temp[k]:
                    break
            else:
                collection.append(m)#m is the index of the first element of the substrings that equal to temp.
        collection.reverse()
        if collection:
            for num in collection:
                if num == 0:
                    gsr_table[i] = i+1
                if num > 0 and p[num-1] != p[i]:
                    gsr_table[i] = i+1-num
            else:
                gsr_table[i] = i+1
        else:
            gsr_table[i] = i+1
    return gsr_table








def good_suffic_rule(p, t):
    '''
    This function is to apply good suffix rule to two sequences with equal length. It returns how many steps should pattern p make to the right.
    p is pattern p, t is a temp slice of text.
    '''
    if p[-1] != t[-1]:
        return 0#This means the good suffix rule do not apply to this case.


