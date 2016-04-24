# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 17:39:05 2016

@author: Coco
"""
from PyQt4.QtGui import *   
from PyQt4.QtCore import *   
import sys   

class TestDialog(QTabWidget):   
    def __init__(self,parent=None):   
        super(TestDialog,self).__init__(parent)   
        
        self.addTab(QCalendarWidget(),"calendar")
        self.addTab(QTableWidget(),"table")
    

app=QApplication(sys.argv)   
dialog=TestDialog()   
dialog.show()   
app.exec_()  