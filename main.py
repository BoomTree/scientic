# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 14:47:33 2016

@author: Coco
"""

import sys 
from PyQt4 import QtGui,QtCore

from forest import Forest
from history import history
from analyze import Analyze

class main(QtGui.QWidget):
    def setupUi(self,Form):
        self.form = Form
        
        Form.resize(300,400)
        Form.setWindowTitle(u'任务中心')
        Form.setStyleSheet('background-color:#CBCBCB')
        #屏幕居中显示
        screen = QtGui.QDesktopWidget().screenGeometry()
        topsize = Form.geometry()
        self.move((screen.width()-topsize.width())/2,(screen.height()-topsize.height())/2)
        
        self.title = QtGui.QLabel(u"电力负荷预测",Form)
        self.title.setStyleSheet("font-size:20px;font-weight:bold;font-family:'微软雅黑';border:1px #FFF")
        self.title.move(90,80)
        
        self.bt1 = QtGui.QPushButton(u'进行电力预测',Form)
        self.bt1.setStyleSheet("font-family:'微软雅黑';font-weight:bold;background-color:#64798F")
        self.bt1.setGeometry(100,140,100,40)
        self.bt1.clicked.connect(self.bt1_clicked)
        
        self.bt2 = QtGui.QPushButton(u'产看历史数据',Form)
        self.bt2.setStyleSheet("font-family:'微软雅黑';font-weight:bold;background-color:#64798F")
        self.bt2.setGeometry(100,200,100,40)
        self.bt2.clicked.connect(self.bt2_clicked)
        
        self.bt3 = QtGui.QPushButton(u'评估预测方法',Form)
        self.bt3.setStyleSheet("font-family:'微软雅黑';font-weight:bold;background-color:#64798F")
        self.bt3.setGeometry(100,260,100,40)
        self.bt3.clicked.connect(self.bt3_clicked)
        
        
    def bt1_clicked(self):
        self.form.hide()
        ui = Forest()
        ui.show()
        ui.exec_()
        self.form.show()
        
    def bt2_clicked(self):
        self.form.hide()
        ui = history()
        ui.show()
        ui.exec_()
        self.form.show()  
        
    def bt3_clicked(self):
        self.form.hide()
        ui = Analyze()
        ui.show()
        ui.exec_()
        self.form.show()
        
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    window = main()  
    window.setupUi(Form)
    Form.show()   
    sys.exit(app.exec_()) 