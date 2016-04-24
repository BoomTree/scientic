# -*- coding: utf-8 -*-
from numpy import random,array,arange,where,diag

"""
Created on Tue Mar 15 21:07:35 2016

@author: Coco
"""
#a = random.rand(3,3)
#print a
#print a[0]
#print a[:,0]
#print a[0,1]
#
#print "------------------------"
#
#b = array([1,2,3,4,5,6,7,8])
#print b[2:8:2]
#print b[-1]
#print b[-3:]
#
#print "------------------------"
#
#c = array([[n+m*10 for n in range(5)] for m in range(5)])
#print c
#print c[1:4,1:4]
#print c[1,2:5]
#
#row_indices = [1,2,3]
#col_indices = [1,2,3]
#e = c[row_indices]
#f = c[row_indices,col_indices]
#print e
#print f

g = arange(0,10,2)
mask = (5<g)*(g<7.5)
print g
print mask
print g[mask]

indices = where(mask)
print indices
print g[indices]

g_diag = diag(g)
g_subdiag = diag(g,-1)
g_subdiag = diag(g,1)
print g_diag
print g_subdiag