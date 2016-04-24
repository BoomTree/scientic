# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 16:51:19 2016

@author: Coco
"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class mainWindow(QWidget):
    def __init__(self, parent = None):
        super(mainWindow, self).__init__(parent)
        button = QPushButton('弹出新窗口', self)
        self.slavewindow = slaveWindow()
        self.connect(button, SIGNAL('clicked()'), self.slavewindow.show)

class slaveWindow(QWidget):
    def __init__(self, parent = None):
        super(slaveWindow, self).__init__(parent)

def main():
    app = QApplication(sys.argv)
    mainwindow = mainWindow()
    mainwindow.show()
    app.exec_()

main()