# -*- coding: utf-8 -*-
from sklearn import datasets,__version__,svm
"""
Created on Wed Mar 23 16:08:24 2016

@author: Coco
"""

iris = datasets.load_iris()
digits = datasets.load_digits()
print type(iris)
print dir(datasets.base.Bunch)
print datasets.base.Bunch.viewitems()
#print digits.target

#print digits.images[1]


clf = svm.SVC(gamma=0.001,C=100.)
clf.fit(digits.data[:-1],digits.target[:-1])
#print clf.predict(digits.data[-1:])