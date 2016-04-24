# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 14:45:56 2016

@author: Coco
"""
import sys
from PyQt4 import QtGui

class Icon(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('icon')
        self.setWindowIcon(QtGui.QIcon('turtle.png'))

app = QtGui.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())