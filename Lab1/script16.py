# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 18:18:20 2016

@author: Егор
"""
#script 16
import collections, re
mas = []
for line in open('data.txt', 'r'):
    mas+= re.findall(r'[A-Za-z]',line)
mas = ''.join(mass)
mas = mas.lower()
print Counter(mas).most_common()
