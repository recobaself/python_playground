#!/usr/bin/python
#coding:utf8

def mysort(x):
    "In this case, x shuld be a string, list or tuple only."
    s = list(x)
    s1 = s[::]
    l = []
    for i in range(len(s)):
        t = max(s1)
        l.append(t)
        s1.remove(t)
    return l

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

def counter(s):
    "This script is used to analyze DNA or Protein sequence."
    l = list(s)
    l1 = [l[0]]
    l2 = [(l[0], l.count(l[0]), format((l.count(l[0]) / len(l)), '.2%'))]
    for i in l:
        if i not in l1:
            m = l.count(i)
            p = format((m / len(l)), '.2%')
            t = (i, m, p)
            l2.append(t)
            l1.append(i)
    print('剔除掉重复的元素以后得： ', l1)
    print('统计元素出现频率得： ', l2)
    result = mysort1(l2)
    print('排序后得： ', result)
    print('分行显示如下： ')
    i = 1
    for item in result:
        print(i, '.', item)
        i += 1

def process(x):
    "This script is used to process DNA sequence for counter function. 这个脚本用来去除DNA序列的空格和换行符号等非法字符。"
    s = ''
    for ea in x:
        if ea in ['a', 't', 'g', 'c', 'A', 'T', 'G', 'C']:
            s += ea
    return s

def mostcommon(s, n):
    "This script is used for analyze the most common element in a sequence."
    l = list(s)
    l1 = [l[0]]
    l2 = [(l[0], l.count(l[0]), format((l.count(l[0]) / len(l)), '.2%'))]
    for i in l:
        if i not in l1:
            m = l.count(i)
            p = format((m / len(l)), '.2%')
            t = (i, m, p)
            l2.append(t)
            l1.append(i)
    result = mysort1(l2)
    for k in range(len(result)):
        if result[k][1] > result[k+1][1]:
            mc = result[:k+1]
            break
    if n == 1:
        for item in mc:
            print(1, '.', item)
    if n > 1:
        print('除去出现频率最高的元素，其余元素的出现频率依次为： ', result[k+1:])
        i = 2
        for item in result[k+1:]:
            print(i, '.', item)
            i += 1

def match(s1, s2):
    '''
    This function is to compare two sequence from the very begining of two sequences and return the slices of matched sequence on the shorter sequence.
    '''
    s = s2 if len(s1) >= len(s2) else s1
    matched = []
    i = 0
    while i < len(s) - 1:
        if s1[i] == s2[i]:
            k = 0
        while i + k <= len(s) - 1:
            if s1[i+k] == s2[i+k]:
                if i + k < len(s) - 1:
                    k += 1
                elif i + k == len(s) - 1:
                    k += 1
                    matched.append((i, i+k))
                    i = i + k
                else:
                    matched.append((i, i+k))
                    i = i + k
                    break
            else:
                i += 1

    return matched

def mismatch(s1, s2):
    '''
    This is the oppsite to match function. In this function, len(s1) == len(s2). The function returns the slices of mismatched sequence.
    '''
    if len(s1) != len(s2):
        return 'The two sequences should have the same length.'
    mismatched = []
    i = 0
    while i < len(s1) - 1:
        if s1[i] != s2[i]:
            k = 0
            while i + k <= len(s1) - 1:
                if s1[i+k] != s2[i+k] and i+k < len(s1) -1:
                    k += 1
                elif s1[i+k] != s2[i+k] and i+k == len(s1) -1:
                    k += 1
                    mismatched.append((i, i+k))
                    i = i + k
                else:
                    mismatched.append((i, i+k))
                    i = i + k
                    break
        else:
            i += 1

    return mismatched


def dna2aa_v1(dna):
    '''
    Translate DNA sequence to amino acide sequence.
    Parameter dna should be a charcter string with no illegal character.
    '''
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

DNA_codon_dict = {'GTT': 'V', 'AGC': 'S', 'AAA': 'K', 'ACT': 'T', 'CAC': 'H', 'CCT': 'P', 'TTG': 'L', 'AGT': 'S', 'CCC': 'P', 'CGT': 'R', 'AAT': 'N', 'GAG': 'E', 'CTT': 'L', 'GGA': 'G', 'GTC': 'V', 'GGC': 'G', 'AAC': 'N', 'TCC': 'S', 'CAT': 'H', 'GGT': 'G', 'GCG': 'A', 'CTC': 'L', 'TAC': 'Y', 'GCA': 'A', 'GGG': 'G', 'ATA': 'I', 'CCA': 'P', 'CTA': 'L', 'ATG': 'M', 'AGA': 'R', 'ACG': 'T', 'GAA': 'E', 'GAT': 'D', 'CTG': 'L', 'TTC': 'F', 'TGG': 'W', 'CAA': 'Q', 'ACC': 'T', 'TTT': 'F', 'ATC': 'I', 'GCT': 'A', 'GTA': 'V', 'CCG': 'P', 'CGC': 'R', 'AGG': 'R', 'TCA': 'S', 'GCC': 'A', 'ATT': 'I', 'TAA': '(STOP)', 'GTG': 'V', 'ACA': 'T', 'TCT': 'S', 'CGA': 'R', 'TGT': 'C', 'TTA': 'L', 'TAT': 'Y', 'AAG': 'K', 'TCG': 'S', 'CGG': 'R', 'GAC': 'D', 'TAG': '(STOP)', 'TGC': 'C', 'TGA': '(STOP)', 'CAG': 'Q'}

def dna2aa(s):
    if len(s) % 3 !=0:
        return 'Please check your sequence to make sure it is 3n bases long.'
    
    s = s.upper()
    for item in s:
        if item not in ['A', 'T', 'G', 'C']:
            return "Illegal character found. ONLY 'A', 'T', 'G', 'C' please."
    aa = ''
    for i in range(0, len(s), 3):
        aa += DNA_codon_dict.get(s[i:i+3]) 
    return aa

def codon2aa(x):
    '''
    This function is to return the amino acide that the input codon codes.
    '''
    if len(x) != 3:
        return 'Failed. Please check your input contains 3 characters.'
    x = x.upper()
    return DNA_codon_dict.get(x, 'Illegal charcter found. Only A, T, G and C are allowed.')

DNA_codon_dict2 = {'K': ('AAA', 'AAG'), 'S': ('TCA', 'TCT', 'TCG', 'TCC', 'AGT', 'AGC'), 
'Arg': ('CGA', 'CGT', 'CGG', 'CGC', 'AGA', 'AGG'), 'Start': ('ATG',), 
'G': ('GGA', 'GGT', 'GGG', 'GGC'), 'Ser': ('TCA', 'TCT', 'TCG', 'TCC', 'AGT', 'AGC'), 
'Trp': ('TGG',), 'Ile': ('ATT', 'ATC', 'ATA'), 'Asn': ('AAT', 'AAC'), 
'R': ('CGA', 'CGT', 'CGG', 'CGC', 'AGA', 'AGG'), 'W': ('TGG',), 'Asp': ('GAT', 'GAC'), 
'N': ('AAT', 'AAC'), 'stop': ('TAA', 'TAG', 'TGA'), 'V': ('GTA', 'GTT', 'GTG', 'GTC'), 
'Leu': ('TTA', 'TTG', 'CTA', 'CTT', 'CTG', 'CTC'), 'Cys': ('TGT', 'TGC'), 
'Stop': ('TAA', 'TAG', 'TGA'), 'Met': ('ATG',), 'Y': ('TAT', 'TAC'), 'H': ('CAT', 'CAC'), 
'T': ('ACA', 'ACT', 'ACG', 'ACC'), 'Val': ('GTA', 'GTT', 'GTG', 'GTC'), 
'Glu': ('GAA', 'GAG'), 'P': ('CCA', 'CCT', 'CCG', 'CCC'), 'C': ('TGT', 'TGC'), 
'Gly': ('GGA', 'GGT', 'GGG', 'GGC'), 'Gln': ('CAA', 'CAG'), 'F': ('TTT', 'TTC'), 
'Phe': ('TTT', 'TTC'), 'E': ('GAA', 'GAG'), 'Ala': ('GCA', 'GCT', 'GCG', 'GCC'), 
'start': ('ATG',), 'Tyr': ('TAT', 'TAC'), 'M': ('ATG',), 'His': ('CAT', 'CAC'), 
'I': ('ATT', 'ATC', 'ATA'), 'Pro': ('CCA', 'CCT', 'CCG', 'CCC'), 'D': ('GAT', 'GAC'), 
'Q': ('CAA', 'CAG'), 'Lys': ('AAA', 'AAG'), 'A': ('GCA', 'GCT', 'GCG', 'GCC'), 
'Thr': ('ACA', 'ACT', 'ACG', 'ACC'), 'L': ('TTA', 'TTG', 'CTA', 'CTT', 'CTG', 'CTC')}

def aa2codon(x):
    '''
    This function is to return the codon for the amino acide.
    '''
    x = x.capitalize()
    return DNA_codon_dict2.get(x, 'Please check your input and make sure it\'s correct.')

def search(p, t):
    '''
    p is pattern, t is the text to be searched using patter sequence.
    '''
    if not p in t:
        return 'No match. Search is done.'
    matched = {'Counts':0, 'Positions':[]}
    for i in range(len(t) - len(p) + 1):
        for k in range(len(p)):
            if t[i+k] != p[k]:
                break
        else:
            matched['Counts'] += 1
            matched['Positions'].append((i, i+len(p)))
    return matched

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
 
RE = {'KpnI':'GGTACC', 'HindIII':'AAGCTT', 'BamHI':'GGATCC', 'BglII':'AGATCT'}

def hairpin(s, length = 4):
    '''
    This function is to identify regions in a DNA sequence that may form hairpin structure.
    '''
    s = s.upper()
    hairpins = []
    for i in range(len(s) - length + 1):
        if r_complement(s[i:i+length]) in s[:i]:
            k = s[:i].find(r_complement(s[i:i+length]))
            slices = (r_complement(s[i:i+length]), s[i:i+length]), (k, k+length), (i, i+length)
        else:
            slices = ()
        if slices and slices not in hairpins:
            hairpins.append(slices)
        if r_complement(s[i:i+length]) in s[i+length:]:
            m = s[i+length:].rfind(r_complement(s[i:i+length])) + i + length
            slices = (s[i:i+length], r_complement(s[i:i+length])), (i, i+length), (m, m+length)
        else:
            slices = ()
        if slices and slices not in hairpins:
            hairpins.append(slices)
    if not hairpins:
        return 0
    if hairpins:
        return hairpins

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

def primers(s, length = 21, f_addon = '', r_addon = ''):
    '''
    This function is to design primers for a DNA sequence.
    The first parameter s is the DNA sequence to be amplified.
    The default value of length of primers is 21-mer.
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

def readfasta(s):
    '''
    This function is to read the fasta file that contains only one record and return a tuple of two parts. The first part is the identifier info, the second part is the sequence.
    The function takes only one parameter 's', which is the filename. The file should be in the working directory.
    read_fasta(s) --> (identifier, seq)
    '''
    foo = open(s, 'r')
    identifier = foo.readline()
    seq = ''
    for line in foo:
    	seq += line.rstrip()
    
    return identifier, seq

def read_multi_fasta(s):
	'''
	This function is to read a fasta file that contains more than one records. A list contains tuples will be returned. In each tuple, two parts are the identifier and the sequence.
	The only parameter the function takes is the file name or the path of the fasta file.
    read_multi_fasta(s) --> [(identifier, seq), ... (identifier, seq)]
	'''
	foo = open(s, 'r')
	line = foo.read()
	foo.close()
	line_split = line.split('>')[1:]
	result = [(item.split('\n', 1)[0], ''.join(item.split('\n')[1:])) for item in line_split]
	return result

def findORF(s):
    '''
    To find all potentially possible ORFs.
    The only parameter s is the DNA sequence to be searched.
    '''
    ORFs = []
    stop = []
    i = s.find('ATG')
    if i == -1:
        return ORFs

    while i <= len(s) - 6:

        k = 3
        while s[i+k:i+k+3] not in ('TAA', 'TAG', 'TGA') and i + k + 3 < len(s):
            k += 3

        else:
            if len(s[i:i+k+3]) % 3 == 0 and s[i:i+k+3][-3:] in ('TAA', 'TAG', 'TGA') and (i+k, i+k+3) not in stop:#原则上一个终止密码子对应一个基因，有多个 ATG 与此终止密码子搭配的话，取长度最长的那个 ATG，其余 ATG 皆是该基因内部的 Met 密码子。
                stop.append((i+k, i+k+3))
                ORFs.append(((i, i+k+3), (str(k+3) + ' bp'), s[i:i+k+3]))
        
        if s[i+3:].find('ATG') == -1:
            return ORFs
        
        i = i + 3 + s[i+3:].find('ATG')
        #n = 3
        #while n < k + 3:
            #if s[i+n:i+n+3] == 'ATG' and n % 3 != 0:
                #i = i + n
                #break
            #n += 1
        #if n >= k+3:
            #if s[i+k+3:].find('ATG') == -1:
                #return ORFs
            #else:
                #i = i + k + 3 + s[i+k+3:].find('ATG')
                   
    return ORFs

def split2rows(s, n, side = None):
    '''
    s is an one-line string. n is an iteger.
    This function split s in to multiple lines, which contains n characters.
    side determin which side of the number goes. Use 'right', 'left', 'R', 'L', or None to tell the function to do its job.
    '''
    def ten(x):
    	'''
    	This function split a string into 10-characters elements.
    	'''
    	i = 0
    	collection = []
    	while i < len(x):
    		collection.append(x[i:i+10])
    		i += 10
    	return ' '.join(collection)

    if side not in ('right', 'left', 'R', 'L', None, 'both', 'B'):
    	return 'Please check the side command.'
    lines = []
    if side in ('right', 'R'):
    	for i in range(0, len(s), n):
    		line = ten(s[i:i+n]) + '  ' + str(i+n) + '\n'
    		lines.append(line)
    	
    elif side in ('left', 'L', None):
    	for i in range(0, len(s), n):
    		line = '%*d'%(8, i+1) + '  ' + ten(s[i:i+n]) + '\n'
    		lines.append(line)
    	
    else:
    	for i in range(0, len(s), n):
    		line = '%*d'%(8, i+1) + '  ' + ten(s[i:i+n]) + '  ' + str(i+n) + '\n'
    		lines.append(line)

    foo = open('splited.txt', 'a')
    foo.writelines(lines)
    foo.close()








    
