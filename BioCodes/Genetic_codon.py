#!/usr/bin/python
#coding:utf8

DNA_codon_dict = {
    ('Ala', 'A'):('GCA','GCT','GCG','GCC'),
    ('Arg', 'R'):('CGA','CGT','CGG','CGC','AGA','AGG'),
    ('Asn', 'N'):('AAT','AAC'),
    ('Asp', 'D'):('GAT','GAC'),
    ('Cys', 'C'):('TGT','TGC'),
    ('Gln', 'Q'):('CAA','CAG'),
    ('Glu', 'E'):('GAA','GAG'),
    ('Gly', 'G'):('GGA','GGT','GGG','GGC'),
    ('His', 'H'):('CAT','CAC'),
    ('Ile', 'I'):('ATT','ATC','ATA'),
    ('Leu', 'L'):('TTA','TTG','CTA','CTT','CTG','CTC'),
    ('Lys', 'K'):('AAA','AAG'),
    ('Met', 'M'):('ATG',),
    ('Phe', 'F'):('TTT','TTC'),
    ('Pro', 'P'):('CCA','CCT','CCG','CCC'),
    ('Ser', 'S'):('TCA','TCT','TCG','TCC','AGT','AGC'),
    ('Thr', 'T'):('ACA','ACT','ACG','ACC'),
    ('Trp', 'W'):('TGG',),
    ('Tyr', 'Y'):('TAT','TAC'),
    ('Val', 'V'):('GTA','GTT','GTG','GTC'),
    ('Start', 'start'):('ATG',),
    ('Stop', 'stop'):('TAA','TAG','TGA')
}

DNA_codon_dict1 = {}
for k, v in DNA_codon_dict.items():
    for item in v:
        DNA_codon_dict1[item] = k[0]

DNA_codon_dict1['ATG'] = 'Met', 'Start'

print(DNA_codon_dict1)


DNA_codon_dict2 = {}
for k, v in DNA_codon_dict.items():
    DNA_codon_dict2[k[0]] = v
    DNA_codon_dict2[k[1]] = v

print(DNA_codon_dict2)

file = open('Genetic_codon_dict.txt', 'w')
file.writelines([str(DNA_codon_dict), '\n', '#'*120, '\n', str(DNA_codon_dict1), '\n', '#'*120, '\n', str(DNA_codon_dict2)])
file.close()

def codon2aa(x):
    '''
    This function is to return the amino acide that the input codon codes.
    '''
    if len(x) != 3:
        return 'Failed. Please check your input contains 3 characters.'
    x = x.upper()
    return DNA_codon_dict1.get(x, 'Illegal charcter found. Only A, T, G and C are allowed.')

def aa2codon(x):
    '''
    This function is to return the codon for the amino acide.
    '''
    x = x.capitalize()
    return DNA_codon_dict2.get(x, 'Please check your input and make sure it\'s correct.')