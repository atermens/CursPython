# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pantalla.ui'
#
# Created: Wed Jul 25 19:46:42 2012
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_pushButton_A(object):
    def setupUi(self, pushButton_A):
        pushButton_A.setObjectName("pushButton_A")
        pushButton_A.resize(568, 327)
        self.centralwidget = QtGui.QWidget(pushButton_A)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 170, 41, 27))
        self.pushButton.setObjectName("pushButton")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 90, 131, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_B = QtGui.QPushButton(self.centralwidget)
        self.pushButton_B.setGeometry(QtCore.QRect(170, 170, 41, 27))
        self.pushButton_B.setObjectName("pushButton_B")
        self.pushButton_C = QtGui.QPushButton(self.centralwidget)
        self.pushButton_C.setGeometry(QtCore.QRect(220, 170, 41, 27))
        self.pushButton_C.setObjectName("pushButton_C")
        self.pushButton_del = QtGui.QPushButton(self.centralwidget)
        self.pushButton_del.setGeometry(QtCore.QRect(70, 70, 98, 27))
        self.pushButton_del.setObjectName("pushButton_del")
        pushButton_A.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(pushButton_A)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 25))
        self.menubar.setObjectName("menubar")
        pushButton_A.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(pushButton_A)
        self.statusbar.setObjectName("statusbar")
        pushButton_A.setStatusBar(self.statusbar)

        self.retranslateUi(pushButton_A)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), lambda : self.AfegeixCar('A'))
        QtCore.QObject.connect(self.pushButton_B, QtCore.SIGNAL("clicked()"), lambda : self.AfegeixCar('B'))
        QtCore.QObject.connect(self.pushButton_C, QtCore.SIGNAL("clicked()"), lambda : self.AfegeixCar('C'))
        QtCore.QObject.connect(self.pushButton_del, QtCore.SIGNAL("clicked()"), lambda: self.Neteja())
        QtCore.QMetaObject.connectSlotsByName(pushButton_A)


    def retranslateUi(self, pushButton_A):
        pushButton_A.setWindowTitle(QtGui.QApplication.translate("pushButton_A", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("pushButton_A", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_B.setText(QtGui.QApplication.translate("pushButton_A", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_C.setText(QtGui.QApplication.translate("pushButton_A", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_del.setText(QtGui.QApplication.translate("pushButton_A", "Del", None, QtGui.QApplication.UnicodeUTF8))


    self.etiq = ''

    def AfegeixCar(self,c):
        self.etiq = self.etiq + c
        self.label.setText(self.etiq)


    def Neteja(self):
	self.etiq = ''
        self.label.setText(self.etiq)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    pushButton_A = QtGui.QMainWindow()
    ui = Ui_pushButton_A()
    ui.setupUi(pushButton_A)
    pushButton_A.show()
    sys.exit(app.exec_())

