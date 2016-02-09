# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 22:30:33 2016

@author: Егор
"""

P = raw_input("Vvedite predlojenie: ")
for i in P:
    if i == '.':
        P = P.replace('.','')
    elif i == ',':
        P = P.replace(',','')
    elif i == '!':
        P = P.replace('!','')
    elif i == '?':    		
        P = P.replace('?','')
P=P.split(' ')
s=''
for x in P:
    if len(x)>7:
        s+=x+' '
for x in P:
    if len(x)>=4 and len(x)<=7:
        s+=x+' '
for x in P:
    if len(x)<4:    
        s+=x+' '       
print s
        

