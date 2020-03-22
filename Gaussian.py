#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:03:13 2020

@author: alanna
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
from random import randint

colors = ['#000000', '#000080', '#00008B', '#008080', '#008B8B', '#4B0082', '#5B0082',
          '#126000', '#777777', '#123456', '#987654', '#101112']
color_face = str(colors[randint(0, len(colors))])
color_edge = str(colors[randint(0, len(colors))+1])

with open('colors.csv') as csvfile:
     colors = csv.reader(csvfile, delimiter=',')
     colors = [','.join(color) for color in colors]



n = int(input("How many gaussian should we simulate? "))
while n <= 10:
    n = int(input("Error, choose another number: "))
x = np.random.randn(n)
plt.hist(x, bins=randint(10, 20), facecolor=color_face, edgecolor=color_edge)
