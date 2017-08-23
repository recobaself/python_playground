#!/usr/bin/python
#coding:utf8

def dna2aa(dna):
    dna = dna.replace('T', 'U')
    l = []
    for i in range(0, len(dna), 3):
        l.append(dna[i : i + 3])
    aa = ''
    for item in l:
        if item in ['GCA','GCU','GCG','GCC']:
            aa += 'A'
        elif item in ['CGA','CGU','CGG','CGC','AGA','AGG']:
            aa += 'R'
        elif item in ['AAU','AAC']:
            aa += 'N'
        elif item in ['GAU','GAC']:
            aa += 'D'
        elif item in ['UGU','UGC']:
            aa += 'C'
        elif item in ['CAA','CAG']:
            aa += 'Q'
        elif item in ['GAA','GAG']:
            aa += 'E'
        elif item in ['GGA','GGU','GGG','GGC']:
            aa += 'G'
        elif item in ['CAU','CAC']:
            aa += 'H'
        elif item in ['AUU','AUC','AUA']:
            aa += 'I'
        elif item in ['UUA','UUG','CUA','CUU','CUG','CUC']:
            aa += 'L'
        elif item in ['AAA','AAG']:
            aa += 'K'
        elif item in ['AUG']:
            aa += 'M'
        elif item in ['UUU','UUC']:
            aa += 'F'
        elif item in ['CCA','CCU','CCG','CCC']:
            aa += 'P'
        elif item in ['UCA','UCU','UCG','UCC','AGU','AGC']:
            aa += 'S'
        elif item in ['ACA','ACU','ACG','ACC']:
            aa += 'T'
        elif item in ['UGG']:
            aa += 'W'
        elif item in ['UAU','UAC']:
            aa += 'Y'
        elif item in ['GUA','GUU','GUG','GUC']:
            aa += 'V'
        elif item in ['UAA','UAG','UGA']:
            aa += '(End)'
    return aa

