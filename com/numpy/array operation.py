# -*- coding: utf-8 -*-
from numpy import array,dot,matrix
"""
Created on Wed Mar 16 12:41:10 2016

@author: Coco
"""

A = array([[n+m*10 for n in range(5)] for m in range(5)])
v1 = range(5)
print A
print v1

#print A+v1
#print A*v1
print A
#print dot(A,A)
print dot(A,v1)


#通过转化成matrix类型进行运算
A_m = matrix(A)
v1_m = matrix(v1).T
print A_m*v1_m