# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 21:21:14 2016

@author: Егор
"""
#script 6
l = raw_input("Vvedite stroky: ")
if l[:3] in 'www':
    l='http://'+l
if l[-4] not in '.com':
    l+='.com'
print l