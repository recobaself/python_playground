#!/usr/bin/python
#coding:utf8

'''
题目：抓了 a, b, c, d 四名犯罪嫌疑人，其中一名是小偷，审讯中：
a 说我不是小偷
b 说 c 是小偷
c 说小偷肯定是 d
d 说 c 胡说
其中有 3 个人说的是实话，一个人说谎。
请编程推断谁是小偷。
'''
for xiaotou in ['a', 'b', 'c', 'd']:
    
    a = bool(xiaotou != 'a')
    b = bool(xiaotou == 'c')
    c = bool(xiaotou =='d')
    d = bool(xiaotou != 'd')
    num = a + b + c + d
    lier_num = 4 - num
    dic = {'a':a, 'b':b, 'c':c, 'd':d}
    lier = [i for i in dic if dic[i] == 0]
    lier_str = ','.join(lier)


    print('如果 %s 是小偷，则有 %d 个人说谎，他们是 %s' % (xiaotou, lier_num, lier_str))