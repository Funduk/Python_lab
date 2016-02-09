# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 10:29:36 2016

@author: Егор
"""
#script 3
N = input("Vvedite float 4islo: ")
if N<0:
   raise NameError('Error') 
N=str(N)
i=N.find('.')
if len(N[i+1:])==1:
    N+='0'
if i==-1:
    N+=' rub.'
    N+=' 00'
else:
    N=N.replace('.', ' rub. ')
print N,' cop.'
