# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 00:34:22 2016

@author: Егор
"""

#script 14
while True:
    try:
        S = raw_input('Vvedite predlogenie: ')     
        if (S[-1]=='.'):
            break
    except:
        print "Error value"
flag = True   
for i in range(len(S)-1):
    for j in range(len(S)):
        if S[i]==S[j] and i!=j: 
            flag = False
            break
    if flag == True and i!=' ':
        print S[i],
    flag = True