# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AWindow(object):
    def setupUi(self, AWindow):
        AWindow.setObjectName("AWindow")
        AWindow.resize(1000, 1000)
        self.centralwidget = QtWidgets.QWidget(AWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 71, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 71, 16))
        self.label.setObjectName("label")
        AWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 446, 20))
        self.menubar.setObjectName("menubar")
        AWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AWindow)
        self.statusbar.setObjectName("statusbar")
        AWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AWindow)
        QtCore.QMetaObject.connectSlotsByName(AWindow)

    def retranslateUi(self, AWindow):
        _translate = QtCore.QCoreApplication.translate
        AWindow.setWindowTitle(_translate("AWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("AWindow", "Gray-Box"))
        self.comboBox.setItemText(1, _translate("AWindow", "White-Box"))
        self.comboBox.setItemText(2, _translate("AWindow", "Black-Box"))
        self.label.setText(_translate("AWindow", "System Mode"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AWindow = QtWidgets.QMainWindow()
    ui = Ui_AWindow()
    ui.setupUi(AWindow)
    AWindow.show()
    sys.exit(app.exec_())
