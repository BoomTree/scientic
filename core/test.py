# -*- coding: utf-8 -*-
"""
Created on Tue Apr 05 15:31:20 2016

@author: Coco
"""
from itertools import chain
from decimal import Decimal
from datetime import date
import numpy as np
a = Decimal('19036.412417')

#print float(a)
#
#b = [[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7]]
#print b[0:1]
#c = {'a':1,'b':2,'c':3,'d':4}
#for key,value in c.iteritems():
#    print key,":",value
#dict =[{'a':1,'b':2,'c':3,'d':4},{'a':1,'b':2,'c':3,'d':4},{'a':1,'b':2,'c':3,'d':4}]
#array = np.array(dict)

#for key,value in c.iteritems():
#    print key," ",value
#    
#for key,value in c.items():
#    
#    print key," ",value
#f = [0,1,2,3,4,5,6,7]
#g = [111,11111,111111]
#f.extend(g)
#f.insert(1,11111)

#print f
#a = date(2007,4,4)
#b = a.isoformat()
#print type(b)
#print b

# a = np.array([[1,2,3,4,5,6],[9,8,7,6,5,4]])
# a = a.reshape(1,-1)
# print id(a)

# a = ['a','b','c','d']
# b = {'a':1,'b':2,'c':3,'d':4}
# # del a[0]
# # print a
# c = b.keys()
# print c
# del c[0]
# print c

# def func_int(a):
#     a += 4
  
# def func_list(a_list):
#     a_list[0] = 4
  
# t = 0
# func_int(t)
# print t
# # output: 0
  
# t_list = [1, 2, 3]
# func_list(t_list)
# print t_list
# # output: [4, 2, 3]

a = [1,2,3,4,5,6,7,8,9,10]
print a[1:]