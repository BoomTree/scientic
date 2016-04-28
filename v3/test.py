# -*- coding: utf-8 -*-
"""
Created on Tue Apr 05 15:31:20 2016

@author: Coco
"""

a = {1:'a',2:'b',3:'c'}
b = {2:'b',3:'c',4:'d'}

x = [0,1,2,3,4,5,6]
y = [7,8,9,10]
z = [11,12,13]
print x
x.extend(y,z)
print x
print y
