#!/usr/bin/python
#coding:utf8

import os
import time
import re

Ala = ['GCA','GCU','GCG','GCC']
Arg = ['CGA','CGU','CGG','CGC','AGA','AGG']
Asn = ['AAU','AAC']
Asp = ['GAU','GAC']
Cys = ['UGU','UGC']
Gln = ['CAA','CAG']
Glu = ['GAA','GAG']
Gly = ['GGA','GGU','GGG','GGC']
His = ['CAU','CAC']
Ile = ['AUU','AUC','AUA']
Leu = ['UUA','UUG','CUA','CUU','CUG','CUC']
Lys = ['AAA','AAG']
Met = ['AUG']
Phe = ['UUU','UUC']
Pro = ['CCA','CCU','CCG','CCC']
Ser = ['UCA','UCU','UCG','UCC','AGU','AGC']
Thr = ['ACA','ACU','ACG','ACC']
Trp = ['UGG']
Tyr = ['UAU','UAC']
Val = ['GUA','GUU','GUG','GUC']
Start = ['AUG']
Stop = ['UAA','UAG','UGA']

def mimazi(s):
    if s in Ala:
        return ('Ala', 'A')
    elif s in Arg:
        return ('Arg', 'R')
    elif s in Asn:
        return ('Asn', 'N')
    elif s in Asp:
        return ('Asp', 'D')
    elif s in Cys:
        return ('Cys', 'C')
    elif s in Gln:
        return ('Gln', 'Q')
    elif s in Glu:
        return ('Glu', 'E')
    elif s in Gly:
        return ('Gly', 'G')
    elif s in His:
        return ('His', 'H')
    elif s in Ile:
        return ('Ile', 'I')
    elif s in Leu:
        return ('Leu', 'L')
    elif s in Lys:
        return ('Lys', 'K')
    elif s in Met:
        return ('Met', 'M')
    elif s in Phe:
        return ('Phe', 'F')
    elif s in Pro:
        return ('Pro', 'P')
    elif s in Ser:
        return ('Ser', 'S')
    elif s in Thr:
        return ('Thr', 'T')
    elif s in Trp:
        return ('Trp', 'W')
    elif s in Tyr:
        return ('Tyr', 'Y')
    elif s in Val:
        return ('Val', 'V')
    elif s in Stop:
        return ('Stop codon')
    else:
        return 'There must be something wrong! Please double check.'

while True:
    codon = raw_input('Please input the codon here:  ')
    if int(len(codon)) != 3:
        print 'The codon should contain 3 elements. :-)'
    elif int(len(codon)) == 3 and codon[0] in 'AaTtGgCcUu' and codon[1] in 'AaTtGgCcUu' and codon[2] in 'AaTtGgCcUu':
        break
    else:
        print 'Only A, U, G, C or T are allowed. :-)'

def capstr(x):
    l = []
    for i in x:
        i = i.capitalize()
        l.append(i)
    return ''.join(l)

codon = capstr(codon)

if 'T' in codon:
    codon = codon.replace('T', 'U')

translation = mimazi(codon)

print translation        

