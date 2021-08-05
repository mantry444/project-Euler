#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 12:21:48 2021

@author: rk
"""
from collections import Counter
l=[]
for i in range (230000000,235000001):
    for j in range (7,21):
       if i% j == 0:
           l.append(i)
 
t=Counter(l)
print (t)        
        
        