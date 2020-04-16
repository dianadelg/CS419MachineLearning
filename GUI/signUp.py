# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignUp.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from User import Ui_UWindow
import login as L

class Ui_SUWindow(object):
    def loginCheck(self):
        user = self.userText.toPlainText()
        passw = self.passText.toPlainText()
        con = self.conText.toPlainText()
        if con == passw:
            res = L.register_DB(user,passw)
            if res == "user":
                self.userText.clear()
                self.passText.clear()
                self.conText.clear()
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_UWindow()
                self.ui.setupUi(self.window)
                self.hide()
                self.window.show()
            else:
                self.userText.clear()
                self.passText.clear()
                self.conText.clear()
                self.errorDisplay.setText("ERROR: Your passwords do not match. Please fix them!!!")
            
    def setupUi(self, SUWindow):
        SUWindow.setObjectName("SUWindow")
        SUWindow.setEnabled(True)
        SUWindow.resize(1000, 1000)
        self.centralwidget = QtWidgets.QWidget(SUWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backBttn = QtWidgets.QPushButton(self.centralwidget)
        self.backBttn.setGeometry(QtCore.QRect(570, 550, 100, 50))
        self.backBttn.setObjectName("backBttn")
        self.signBttn = QtWidgets.QPushButton(self.centralwidget)
        self.signBttn.setGeometry(QtCore.QRect(730, 550, 100, 50))
        self.signBttn.setObjectName("signBttn")
        self.signBttn.clicked.connect(self.loginCheck)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 136, 800, 400))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.passText = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.passText.setObjectName("passText")
        self.gridLayout.addWidget(self.passText, 5, 0, 1, 1)
        self.userLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.userLabel.setObjectName("userLabel")
        self.gridLayout.addWidget(self.userLabel, 2, 0, 1, 1)
        self.passLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.passLabel.setObjectName("passLabel")
        self.gridLayout.addWidget(self.passLabel, 4, 0, 1, 1)
        self.conText = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.conText.setObjectName("conText")
        self.gridLayout.addWidget(self.conText, 7, 0, 1, 1)
        self.userText = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.userText.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userText.sizePolicy().hasHeightForWidth())
        self.userText.setSizePolicy(sizePolicy)
        self.userText.setMinimumSize(QtCore.QSize(0, 0))
        self.userText.setObjectName("userText")
        self.gridLayout.addWidget(self.userText, 3, 0, 1, 1)
        self.conLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.conLabel.setObjectName("conLabel")
        self.gridLayout.addWidget(self.conLabel, 6, 0, 1, 1)
        self.errorDisplay = QtWidgets.QTextEdit(self.centralwidget)
        self.errorDisplay.setGeometry(QtCore.QRect(40, 43, 700, 50))
        self.errorDisplay.setReadOnly(True)
        self.errorDisplay.setObjectName("errorDisplay")
        SUWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SUWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 20))
        self.menubar.setObjectName("menubar")
        SUWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SUWindow)
        self.statusbar.setObjectName("statusbar")
        SUWindow.setStatusBar(self.statusbar)
        self.retranslateUi(SUWindow)
        QtCore.QMetaObject.connectSlotsByName(SUWindow)

    def retranslateUi(self, SUWindow):
        _translate = QtCore.QCoreApplication.translate
        SUWindow.setWindowTitle(_translate("SUWindow", "MainWindow"))
        self.backBttn.setText(_translate("SUWindow", "Back"))
        self.signBttn.setText(_translate("SUWindow", "Sign-Up"))
        self.userLabel.setText(_translate("SUWindow", "UserName"))
        self.passLabel.setText(_translate("SUWindow", "Password"))
        self.conLabel.setText(_translate("SUWindow", "Confirm Password"))
        self.errorDisplay.setHtml(_translate("SUWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Please type the username and password you\'d like!!</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SUWindow = QtWidgets.QMainWindow()
    ui = Ui_SUWindow()
    ui.setupUi(SUWindow)
    SUWindow.show()
    sys.exit(app.exec_())
