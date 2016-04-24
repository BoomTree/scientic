# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 15:30:13 2016

@author: Coco
"""
import sys
from PyQt4 import QtGui,QtCore
class MainWindow(QtGui.QMainWindow):
    def setStatusMsg(self,msg):
        self.statusBar().showMessage(msg)
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        
        self.resize(400,300)
        self.setWindowTitle('mainwindow')
        
        #显示在屏幕中央显示
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

        #底部状态栏
        self.statusBar().showMessage('as')
        
        #添加exit
        exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        exit.connect(exit, QtCore.SIGNAL('triggered()'), QtGui.qApp,
        QtCore.SLOT('quit()'))
        #添加File
        menubar = self.menuBar()
        file = menubar.addMenu('&File')
#        将eixt添加进File
        file.addAction(exit)

        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

app = QtGui.QApplication(sys.argv)
mw = MainWindow()
mw.show()
sys.exit(app.exec_())