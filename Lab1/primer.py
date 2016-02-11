# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 10:27:35 2016

@author: Егор
"""

import math
N = 0
mas = []
flag = False
for N in range(1,100000):
    for i in range(100):
        for j in range(100):
            for k in range(100):
                sum = math.pow(i,3)+math.pow(j,3)+math.pow(k,3)
                if (sum==N):
                    m = [i,j,k,sum]
                    print m
                    mas.append(m)
                    flag = True
                

if (flag==False):
    print "Nothing to find"
else:
    for i in range(len(mas)):
        count = 0
        number = mas[i][3]
        for j in range(len(mas)):
            if (mas[j][3]==number):
                count+=1
        
        if (count>=3):
            print "["+str(number)+"]="+str(count)
            continue