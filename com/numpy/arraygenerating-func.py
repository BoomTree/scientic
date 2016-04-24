# -*- coding: utf-8 -*-

from numpy import arange,linspace,array,random,diag

"""
Created on Tue Mar 15 15:54:53 2016

@author: Coco
"""
a = arange(0,10,5)
b = linspace(0,10,25)
c,d = mgrid[0:5,0:5]

print a
print b
print c,d

print random.randn(5,5)

print diag([1,3,4],1)