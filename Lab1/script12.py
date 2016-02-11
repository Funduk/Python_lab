# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:17:40 2016

@author: Егор
"""
#script 12
for N in range(1,100000):
    m=[]
    mas=[]
    x = y = z = k = 0
    st=int(N**(1/3.0)+2)
    for z in range(0,st):
        for y in range(z,st):
            for x in range(y,st):
                if x**3+y**3+z**3==N:
                    m = [x, y, z]
                    mas += list(map(lambda i: m[3*i:(i+1)*3], range(1)))
                    k+=1
    if(k>=3):
        print N, mas