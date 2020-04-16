# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UWindow(object):
    def setupUi(self, UWindow):
        UWindow.setObjectName("UWindow")
        UWindow.resize(1000, 1000)
        self.centralwidget = QtWidgets.QWidget(UWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 160, 101, 61))
        self.label.setObjectName("label")
        UWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 446, 20))
        self.menubar.setObjectName("menubar")
        UWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UWindow)
        self.statusbar.setObjectName("statusbar")
        UWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UWindow)
        QtCore.QMetaObject.connectSlotsByName(UWindow)

    def retranslateUi(self, UWindow):
        _translate = QtCore.QCoreApplication.translate
        UWindow.setWindowTitle(_translate("UWindow", "MainWindow"))
        self.label.setText(_translate("UWindow", "This is the User Screen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UWindow = QtWidgets.QMainWindow()
    ui = Ui_UWindow()
    ui.setupUi(UWindow)
    UWindow.show()
    sys.exit(app.exec_())
