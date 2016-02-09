# -*- coding: utf-8 -*-
"""
Created on Sun Feb 07 21:55:41 2016

@author: Егор
"""

#script 1
N = input("Vvedite 4islo ot 1 do 100: ")
if N<0:
    print("Error")
elif N>10 and N<15:
    print N, " let"
else:
    N=str(N)
    if N[-1]=='1':
        print N, " god"
    elif N[-1]>='2' and N[-1]<='4':
        print N," goda"
    elif (N[-1]>='5' and N[-1]<='9') or (N[-1]=='0'):
        print N," let"


