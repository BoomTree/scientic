# -*- coding: utf-8 -*-

from numpy import linspace
from scipy.special import jn,yn,jn_zeros,yn_zeros
import matplotlib.pyplot as plt
"""
Created on Wed Mar 16 14:28:56 2016

@author: Coco
"""
x = linspace(0,10,100)


fig,ax = plt.subplots()
for n in range(4):
    ax.plot(x,jn(n,x),label=r"$J_%d(x)$" % n)
ax.legend();

n = 0
m = 4
print jn_zeros(n,m)