# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 22:13:23 2016

@author: Егор
"""
#script 13
while True:
    try:
        S = raw_input('Vvedite predlogenie: ')     
        if (S[-1]=='.'):
            break
    except:
        print "Error value"
Sp = S.split(' ')        
print Sp,'\n', S
S = ''
n=1
for i in Sp:
    if (i[-1]=='.') or (i[-1]==','):
        S += i[0:-1] + '(' + str(n) + ')' + i[-1] + ' '
        n+=1
    elif i=='-':
        S += '- '
    else:
        S += i + '(' + str(n) + ') '
        n+=1
print S