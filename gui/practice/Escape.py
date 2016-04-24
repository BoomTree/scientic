# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 16:15:11 2016

@author: Coco
"""

import sys
from PyQt4 import QtGui, QtCore

class Escape(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle('escape')
        self.resize(250, 150)
        self.connect(self, QtCore.SIGNAL('closeEmitApp()'),QtCore.SLOT('close()'))
        
    def mousePressEvent(self, event):
        self.emit(QtCore.SIGNAL('closeEmitApp()'))

app = QtGui.QApplication(sys.argv)
qb = Escape()
qb.show()
sys.exit(app.exec_())