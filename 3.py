#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#import math 
a= int(input())
c=int ((a/3))
#b= int (math.sqrt(a))
#print (c)
x=[]
for i in range (2,c+1):
    if a % i ==0 :
        print (i)

x=[i]
print (x)        