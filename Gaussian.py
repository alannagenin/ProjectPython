#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:03:13 2020

@author: alanna
"""

import numpy as np
import matplotlib.pyplot as plt
from random import randint

#list of colors
colors = ['#586BA4', '#000080', '#00008B', '#008080', '#008B8B', '#4B0082', '#5B0082',
          '#126000', '#777777', '#123456', '#987654', '#101112', '#665687', '#190933',
          '#5D576B', '#FE938C', '#D496A7', '#007EA7', '#003249', '#5B2A86', '#7785AC',
          '#FF521B', '#F61067', '#6DECAF', '#3D52D5', '#247BA0', '#2A0C4E', '#F76C5E']

#choose randomly two colors
color1 = str(colors[randint(0, len(colors))])
color2 = str(colors[randint(0, len(colors))+1])


#ask how many gaussians simulate
def user_input():
    n = int(input("How many gaussian should we simulate? "))
    while n <= 10:
        n = int(input("Error, choose another number: "))
    return n

def ploting(n, color):
    plt.hist(np.random.randn(n), bins=randint(10, 20), facecolor=color, edgecolor=color)
    plt.show()
            
if __name__ == "__main__":
    n = user_input()
    ploting(n, color1)
    ploting(n, color2)