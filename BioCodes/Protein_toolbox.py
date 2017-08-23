#!/usr/bin/python
#coding:utf8

AA_list = ['A', 'C', 'E', 'D', 'G', 'F', 'I', 'H', 'K', 'M', 'L', 'N', 'Q', 'P', 'S', 'R', 'T', 'W', 'V', 'Y']

def process(s):
    '''
    This function is to remove illegal characters in the string.
    The processed string will be ready for further operations.
    This function is only for protein sequences that contain exclusively the regular 20 amino acids.
    '''
    s = s.upper()
    seq = ''
    for item in s:
        if item in AA_list:
            seq += item
    return seq

def AA_Counter(s):
    '''
    This functions calculate the occurence number of each amino acid and return a sorted list according to occurence number. 
    Before run this function, the sequence should have been processed in advance.
    '''
    s = s.upper()
    AA_dict = {}

    for item in AA_list:
        AA_dict[item] = [0]

    for aa in s:
        AA_dict[aa][0] += 1

    for k, v in AA_dict.items():
        v.append(format(float(v[0])/len(s), '.2%'))

    return sorted(AA_dict.items(), key = lambda item : item[1][0], reverse = True)

