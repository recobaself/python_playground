#!/usr/bin/python
#coding:utf8
print "请按照提示输入数字，待计算的量请用 X 代替。"
a = raw_input("请输入待溶解的溶质的质量（单位：mg）: ")
b = raw_input("请输入溶剂的体积（单位：ml）: ")
c = raw_input("请输入最终浓度（单位：mg/ml）: ")

if a == "X":
    X = float(b)*float(c)
    print "所需溶质的质量为：", X, "mg"

if b == "X":
    X = float(a)/float(c)
    print "所需溶剂的体积为：", X, "ml"

if c == "X":
    X = float(a)/float(b)
    print "最终所得浓度为：", X, "mg/ml"

print "计算完毕。"
