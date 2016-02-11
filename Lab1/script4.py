# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 13:17:35 2016

@author: Егор
"""

#script 4
N = input("Vvedite N: ")
pi=1
x=1
while x !=N:
    f=float(2*x+1)
    if x%2==1:
        pi-=1/f
    else:
        pi+=1/f
    x+=1
pi=pi*4
print pi
    