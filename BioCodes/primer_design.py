#!/usr/bin/python
#coding:utf8

def GC_content(s):
    '''
    Calculate GC content of DNA.
    '''
    s = s.upper()
    G_content = s.count('G')
    C_content = s.count('C')
    ratio = (G_content + C_content) / float(len(s))
    return format(ratio, '.2%')

def r_complement(s):
    s = s.upper()
    dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    rc_s = ''
    for base in s:
        rc_s = dict[base] + rc_s
    return rc_s

RE = {'HindIII':'AAGCTT', 'BamHI':'GGATCC', 'BglII':'AGATCT'}

def primers(s, length = 21, f_addon = '', r_addon = ''):
    '''
    This function is to design primers for a DNA sequence.
    '''
    s = s.upper()
    for base in s:
    	if not base in ['A', 'T', 'G', 'C']:
    		break
    		return 'Illegal character found. Please check your sequence.'
    result = [[],[],[]]
    f_primer = f_addon + s[0:length]
    r_primer = r_addon + r_complement(s[-length:])
    attr = [(str(length) + '-' + 'mer'), {'f_primer_GC':GC_content(f_primer)}, {'r_primer_GC':GC_content(r_primer)}]
    result[0].extend(attr)
    result[1].append({'f_primer':f_primer})
    result[2].append({'r_primer':r_primer})
    return result

    