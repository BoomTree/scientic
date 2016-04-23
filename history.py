# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 21:18:00 2016

@author: Coco
"""

from PyQt4 import QtCore, QtGui

class history(QtGui.QWidget):
    def setupUi(self, Dialog):
        self.form = Dialog   
        Dialog.resize(300,400)
        Dialog.setWindowTitle(u'任务中心')
        Dialog.setStyleSheet('background-color:#F0F0F0')
        #屏幕居中显示
        screen = QtGui.QDesktopWidget().screenGeometry()
        topsize = Dialog.geometry()
        Dialog.move((screen.width()-topsize.width())/2,(screen.height()-topsize.height())/2)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = history()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())