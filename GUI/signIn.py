# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signIn.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Admin import Ui_AWindow
from User import Ui_UWindow
import login as L
class Ui_SIWindow(object):
    
    def loginCheck(self):
        user = self.userText.toPlainText()
        passw = self.passText.toPlainText()
        res = L.login(user,passw)
        if res == "user":
            self.userText.clear()
            self.passText.clear()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_UWindow()
            self.ui.setupUi(self.window)
            self.hide()
            self.window.show()
        elif res == "admin":
            self.userText.clear()
            self.passText.clear()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_AWindow()
            self.ui.setupUi(self.window)
            self.hide()
            self.window.show()
        #else:
            

    def setupUi(self, SIWindow):
        SIWindow.setObjectName("SIWindow")
        SIWindow.resize(1000, 1000)
        self.centralwidget = QtWidgets.QWidget(SIWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.signBttn = QtWidgets.QPushButton(self.centralwidget)
        self.signBttn.setGeometry(QtCore.QRect(730, 550, 100, 50))
        self.signBttn.setObjectName("signBttn")
        self.signBttn.clicked.connect(self.loginCheck)
        self.backBttn = QtWidgets.QPushButton(self.centralwidget)
        self.backBttn.setGeometry(QtCore.QRect(570, 550, 100, 50))
        self.backBttn.setObjectName("backBttn")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 126, 800, 400))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.userLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.userLabel.setObjectName("userLabel")
        self.gridLayout.addWidget(self.userLabel, 0, 0, 1, 1)
        self.userText = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.userText.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userText.sizePolicy().hasHeightForWidth())
        self.userText.setSizePolicy(sizePolicy)
        self.userText.setObjectName("userText")
        self.gridLayout.addWidget(self.userText, 3, 0, 1, 1)
        self.passLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.passLabel.setObjectName("passLabel")
        self.gridLayout.addWidget(self.passLabel, 4, 0, 1, 1)
        self.passText = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.passText.setObjectName("passText")
        self.gridLayout.addWidget(self.passText, 5, 0, 1, 1)
        SIWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SIWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 446, 20))
        self.menubar.setObjectName("menubar")
        SIWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SIWindow)
        self.statusbar.setObjectName("statusbar")
        SIWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SIWindow)
        QtCore.QMetaObject.connectSlotsByName(SIWindow)

    def retranslateUi(self, SIWindow):
        _translate = QtCore.QCoreApplication.translate
        SIWindow.setWindowTitle(_translate("SIWindow", "MainWindow"))
        self.signBttn.setText(_translate("SIWindow", "Sign-In"))
        self.backBttn.setText(_translate("SIWindow", "Back"))
        self.userLabel.setText(_translate("SIWindow", "UserName"))
        self.passLabel.setText(_translate("SIWindow", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SIWindow = QtWidgets.QMainWindow()
    ui = Ui_SIWindow()
    ui.setupUi(SIWindow)
    SIWindow.show()
    sys.exit(app.exec_())
