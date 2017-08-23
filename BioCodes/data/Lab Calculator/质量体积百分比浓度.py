#!/usr/bin/python
#coding:utf8
#质量体积百分比浓度

print '请根据提示输入信息，待求的项请用 X 替代。'
a = raw_input('请输入质量浓度百分比（普通小数格式）: ')
b = raw_input('请输入最终体积（单位： ml）: ')
c = raw_input('请输入称量的溶质质量（单位： g）: ')

if a == 'X':
    print '质量体积百分比浓度为： ', format(float(c)/b, '.2%')
if b == 'X':
    print '该溶液的最终体积应为： ', float(c)/a, 'ml'
if c == 'X':
    print '所需溶质质量应为： ', float(b) * float(a), 'g'