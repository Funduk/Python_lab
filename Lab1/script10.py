# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 00:55:25 2016

@author: Егор
"""

arr = list(input('Vvedite massiv: '))
flag = True
i=1
while i != len(arr)-1:
    if int(arr[i+1])<int(arr[i]):
        flag=False
    i+=1
print flag