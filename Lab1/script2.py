# -*- coding: utf-8 -*-
"""
Created on Sun Feb 07 22:38:33 2016

@author: Егор
"""

#script 2
date = list(input("Vvedite dd mm yyyy: "))
for x in range(3):
    if date[x]<1:
        raise NameError('Error')
    date[x]=str(date[x])
    if len(date[x])==1 and date[x]!=date[2]:
        date[x]='0'+date[x]    

date = '/'.join(date)
print date
