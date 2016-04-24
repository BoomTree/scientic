# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableFrame.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(712, 408)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 711, 411))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "新建列", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "日期", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "天气类型", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "新建列", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "平均气压", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "最高气压", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "最低气压", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "平均气温", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "最低气温", None))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "20-20时降雨量", None))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "新建列", None))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Form", "日照时数", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

