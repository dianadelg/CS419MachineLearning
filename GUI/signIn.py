from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SIWindow(object):

    def setupUi(self, SIWindow):
        SIWindow.setObjectName("SIWindow")
        SIWindow.resize(1000, 1000)
        self.centralwidget = QtWidgets.QWidget(SIWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.signBttn = QtWidgets.QPushButton(self.centralwidget)
        self.signBttn.setGeometry(QtCore.QRect(730, 550, 100, 50))
        self.signBttn.setObjectName("signBttn")
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
        self.errorDisplay = QtWidgets.QTextEdit(self.centralwidget)
        self.errorDisplay.setGeometry(QtCore.QRect(40, 43, 800, 55))
        self.errorDisplay.setReadOnly(True)
        self.errorDisplay.setObjectName("errorDisplay")
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
        self.errorDisplay.setHtml(_translate("SIWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Please type in your username and password!!</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SIWindow = QtWidgets.QMainWindow()
    ui = Ui_SIWindow()
    ui.setupUi(SIWindow)
    SIWindow.show()
    sys.exit(app.exec_())
