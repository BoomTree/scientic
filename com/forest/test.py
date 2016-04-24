# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:24:32 2016

@author: Coco
"""

import sys

#!!!practice  function map()
def formate(name):
    str = ''
    for value in range(len(name)):
        if value==0:
            str += name[value].upper()
        else:
            str += name[value].lower()
    return str
#print formate(name='sdf')
#print map(formate,['sfd','WEf',"sfe2r"])


#!!!practice  function reduce()
def multiply(a,b):
    return a*b
#print reduce(multiply,[2,34,5,61,3])


#!!!practice  function filter()
def is_odd(a):
    return a%2==1
#print filter(is_odd,[2,43,513,3,3,3432,34])


data = [{"a":1,"b":2},{"a":3,"b":4}]
for row in data:
    row['a'] = 5
for row in data:
    print row['a']