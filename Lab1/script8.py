# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 22:30:33 2016

@author: Егор
"""

P = raw_input("Vvedite predlojenie: ")
P=P.split(' ')
for x in P:
    if len(x)>7:
        print x
for x in P:
    if len(x)>=4 and len(x)<=7:
        print x
for x in P:
    if len(x)<4:    
        print x
