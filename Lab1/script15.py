# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 15:52:44 2016

@author: Егор
"""
#script 15
import re
print re.findall(r'\b[A-Z][a-zA-z]+\d{2}\b',raw_input('Vvedite stroky: '))