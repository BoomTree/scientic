# -*- coding: utf-8 -*-

from numpy import array,genfromtxt,random,savetxt,save,loads
import matplotlib.pyplot as plt
"""
Created on Tue Mar 15 18:50:12 2016

@author: Coco
"""

data = genfromtxt('stockholm_td_adj.dat')

print data.shape
print data.__class__
print data.size
print data.dtype

fig,ax = plt.subplots(figsize=(14,4))
ax.plot(data[:,0]+data[:,1]/12.0+data[:,2]/365,data[:,5])
ax.axis('tight')
ax.set_title('tempeatures in Stockholm')
ax.set_xlabel('year')
ax.set_ylabel('temperature (C)');
#
#p = random.rand(3,3,3,3)
#m = random.rand(3,3)
#
#print m
#
##savetxt("random-matrix.csv",m,fmt='%.5f')
##save("random-matrix.npy",m)
#
#b = load("random-matrix.npy")
#print b
#print "itemsize:",b.itemsize
#print "nbytes:",b.nbytes
#print "ndim:",p.ndim  # dimension 纬度
#
#
#
