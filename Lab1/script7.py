# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 20:53:09 2016

@author: Егор
"""
#script 7
N = raw_input("Vvedite nomer carti (16 cifr): ")
if len(N) == 16:
	print N.replace(N[4:12], '********')
else:
	print "Ti 4o debil? 16 cifr podryad! "

