# -*- coding: utf-8 -*-   
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
import sys  
import leftLayout
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  
  
class LayoutDialog(QDialog):  
    def __init__(self,parent=None):  
        super(LayoutDialog,self).__init__(parent)  
        self.setWindowTitle(self.tr("电力负荷预测系统"))
        
        main=QHBoxLayout()
        ly = leftLayout.leftLayout(self)
        
        main.addWidget(ly)  
        main.addWidget(ly)  
#        mainLayout.addLayout(rightLayout,0,1)  




QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))
app=QApplication(sys.argv)
dialog=LayoutDialog()
dialog.show()
app.exec_()