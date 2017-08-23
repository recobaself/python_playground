#!/usr/bin/python
#coding:utf8
print 'Please input the following values. Use X to represent the one you are pursuing.'
a = raw_input("please input final concentration (单位：mM): ")
b = raw_input("please input the volume (单位：mL): ")
c = raw_input("please input the molecular weight (g/mol): ")
d = raw_input("please input the weight(单位：g): ")

if a == "X":
    X= float(d)/float(c)/float(b)*1000*1000
    print "X=", X, "mM"

if b == "X":
    X= float(d)/float(a)/float(c)*1000*1000
    print "X=", X, "mL"

if d == "X":
    X= float(a)*float(b)*float(c)/1000/1000
    print "X =", X, "g"
