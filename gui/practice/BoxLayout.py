# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 15:52:32 2016

@author: Coco
"""

import sys 
from PyQt4 import QtGui

class BoxLayout(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self)
        
        self.setWindowTitle('box layout')
        ok = QtGui.QPushButton('OK')
        cancel = QtGui.QPushButton('Cancel')
        
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(ok)
        hbox.addWidget(cancel)
        
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        self.resize(300,160)
        
app = QtGui.QApplication(sys.argv)
qb = BoxLayout()
qb.show()
sys.exit(app.exec_())