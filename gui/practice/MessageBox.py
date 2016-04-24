# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 15:15:16 2016

@author: Coco
"""

import sys
from PyQt4 import QtGui

class MessageBox(QtGui.QMessageBox):
    def __init__(self,parent=None):
        QtGui.QMessageBox.__init__(self,parent)
        self.resize(250,150)
        self.setWindowTitle('messageBox')
        
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
        
    def closeEvent(self,event):
        reply = QtGui.QMessageBox.question(self,'Message','are you sure to quit?',QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
app = QtGui.QApplication(sys.argv)
mb = MessageBox()
mb.show()
sys.exit(app.exec_())