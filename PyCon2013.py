#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:37:34 2020

@author: alanna
"""

#tools to use : iter, partial

#Looping integers
print("Square : ")
for i in [0, 1, 2, 3, 4, 5, 6]:
   print(i**2)

#better 
print("\nBetter version :")   
for i in range(7):
    print(i**2)

#better but ugly --> doesn't exists anymore
#for i in xrange(7):
#    print(i**2)
    
#Looping over a collection    
print("\nColors :")
colors = ['red', 'green', 'blue', 'yellow']
for i in range(len(colors)):
    print(colors[i])
    
#better and faster
print("\nBetter version for colors :")
for color in colors:
    print(color) 