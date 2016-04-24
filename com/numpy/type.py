# -*- coding: utf-8 -*-
 %load_ext version_information
"""
Created on Tue Mar 15 14:48:18 2016

@author: Coco
"""

def powers(a):
    """
    return a few powers of a
    """
    return a**2,a**3,a**4

powerscp = lambda x: (x**2,x**3)
    
print powerscp(3).__class__

try:
    print "adf"
    print asdf`
except Exception as asdf:
    print asdf.message

print %version_information