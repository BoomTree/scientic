# -*- coding: utf-8 -*-
import numpy as np
import math
from sklearn import metrics
from sklearn.svm import SVC
from stage2 import atmsList,tomorrowAtmList
"""
Created on Fri Mar 25 12:35:05 2016

@author: Coco
"""

dataset = np.array(atmsList)
X = dataset[:,0:11]
y = dataset[:,12]
ta = np.array(tomorrowAtmList)
ta_X = ta[0:11]
ta_X = ta_X.reshape(1,-1)
ta_y = ta[12]
#print type(X)
#print type(y)
model = SVC()
#print model
model.fit(X, y)
expected = ta_y
predicted = model.predict(ta_X)
print expected
print predicted

print abs(expected - predicted)/expected
#for index in range(len(expected)):
#    if(expected[index] == predicted[index]):
#        print 1
#    else:
#        print 0
def abs(num):
    if num<0:
        return num*-1
    return num
#print(metrics.classification_report(expected, predicted))
#print(metrics.confusion_matrix(expected, predicted))