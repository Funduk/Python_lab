# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 23:06:06 2016

@author: Егор
"""
import random
N = random.randint(1,1000)
print 'Razmer massiva: ', N
arr=[]
x=0
while x != N:
    arr+=[random.randint(1,1000)]
    x+=1
too=[]
min = 512
for i in range(11)  :
    too+=[2**i]
    if (2**i-N)<min and (2**i-N)>=0:
        min=2**i-N
        st=too[i]
arr+=[0]*min
print 'Blijashaya stepen: ', st  
print 'Kol-vo 0: ', min
print arr
