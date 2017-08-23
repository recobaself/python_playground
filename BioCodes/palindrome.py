#!/usr/bin/python
#coding:utf8

def palindrome(s):
    '''
    This function is to test whether a sequence is a palindromic loop. If yes, return 1, otherwise 0.
    '''
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    s = s.upper()
    for i in range(len(s)):
        if s[i] != complement[s[len(s) - 1 - i]]:
            return 0
    else:
        return 1

def find_palindrome(s, length = 6):
    '''
    This function is to search palindromic loops across the sequence.
    Default length for the palindromic loop is 6.
    '''
    s = s.upper()
    palindromic = {}
    for i in range(len(s) - length + 1):
        if palindrome(s[i:i+length]):
            if s[i:i+length] not in palindromic.keys():
                palindromic[s[i:i+length]] = 1
            else:
                palindromic[s[i:i+length]] += 1
    return sorted(palindromic.items(), key=lambda item : item[1], reverse = True)
