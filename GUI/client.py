# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CWindow(object):
        
    def setupUi(self, CWindow):
        CWindow.setObjectName("CWindow")
        CWindow.resize(1000, 1000)
        self.centralwidget = QtWidgets.QWidget(CWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.displayUser = QtWidgets.QLabel(self.centralwidget)
        self.displayUser.setGeometry(QtCore.QRect(80, 150, 900, 65))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.displayUser.setFont(font)
        self.displayUser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.displayUser.setObjectName("displayUser")
        self.signInButton = QtWidgets.QPushButton(self.centralwidget)
        self.signInButton.setGeometry(QtCore.QRect(400, 270, 230, 55))
        self.signInButton.setObjectName("signInButton")
        self.signUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.signUpButton.setGeometry(QtCore.QRect(400, 368, 230, 55))
        self.signUpButton.setObjectName("signUpButton")
        CWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 446, 20))
        self.menubar.setObjectName("menubar")
        CWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CWindow)
        self.statusbar.setObjectName("statusbar")
        CWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CWindow)
        QtCore.QMetaObject.connectSlotsByName(CWindow)

    def retranslateUi(self, CWindow):
        _translate = QtCore.QCoreApplication.translate
        CWindow.setWindowTitle(_translate("CWindow", "MainWindow"))
        self.displayUser.setText(_translate("CWindow", "Would You like to Sign-in or Sign-Up?"))
        self.signInButton.setText(_translate("CWindow", "Sign-in"))
        self.signUpButton.setText(_translate("CWindow", "Sign-up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CWindow = QtWidgets.QMainWindow()
    ui = Ui_CWindow()
    ui.setupUi(CWindow)
    CWindow.show()
    sys.exit(app.exec_())
