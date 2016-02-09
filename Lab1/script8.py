# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 22:30:33 2016

@author: Егор
"""

P = raw_input("Vvedite predlojenie: ")
P=P.split(' ')
for x in P:
    if len(P[x])>7:
        print P[x]
for x in len(P):
    if len(P[x])>=4 and len(P[x])<=7:
        print P[x]
for x in len(P):
    if len(P[x])<4:
        print P[x]
