#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 19:55:51 2021

@author: rk
"""

for i in range (100,1000) :
    for j in range (100,1000):
      x= i*j
      if 900000< x <998001:
        a= x
        k1= a
        k2=str(k1)
        k3=k2[::-1]
        k4=int(k3)
        if k4==k1:
            
          print(a)       

       