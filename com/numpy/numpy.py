# -*- coding: utf-8 -*-

from numpy import *
from math import pi,cos

import types

v = array([1L,3L,4L],dtype=long)
m = array([[1,2],[3,4]])
a = arange(0,10,1)
t = array([[[1,2],[3,4]],[[5,6],[7,8]],[[5,6],[7,8]],[[5,6],[7,8]]])
print v
print m
print a
print t

x = math.cos(2*math.pi)
y = cos(pi)
print x,y

help(math.log)
help(math.ceil)

print type(v)
#print dir(types)
print v.shape,m.shape,a.shape,t.shape
print v.size,m.size,size(a),t.size
print v.dtype,m.dtype,a.dtype,t.dtype
