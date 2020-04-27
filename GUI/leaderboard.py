from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LWindow(object): 
        
    def setupUi(self, LWindow):
        LWindow.setObjectName("LWindow")
        LWindow.resize(1300, 1100)
        self.centralwidget = QtWidgets.QWidget(LWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.leaderboardDisplay = QtWidgets.QTableWidget(self.centralwidget)
        self.leaderboardDisplay.setGeometry(QtCore.QRect(10, 10, 1050, 1050))
        self.leaderboardDisplay.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.leaderboardDisplay.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.leaderboardDisplay.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.leaderboardDisplay.setObjectName("leaderboardDisplay")
        self.leaderboardDisplay.setColumnCount(4)
        self.leaderboardDisplay.setRowCount(20)
        self.leaderboardDisplay.setEnabled(True)
        self.updateBttn = QtWidgets.QPushButton(self.centralwidget)
        self.updateBttn.setGeometry(QtCore.QRect(1100, 525, 170, 100))
        self.updateBttn.setObjectName("updateBttn")
        item = QtWidgets.QTableWidgetItem()
        self.leaderboardDisplay.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.leaderboardDisplay.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.leaderboardDisplay.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.leaderboardDisplay.setHorizontalHeaderItem(3, item)
        LWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 446, 22))
        self.menubar.setObjectName("menubar")
        LWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LWindow)
        self.statusbar.setObjectName("statusbar")
        LWindow.setStatusBar(self.statusbar)
        self.retranslateUi(LWindow)
        QtCore.QMetaObject.connectSlotsByName(LWindow)

    def retranslateUi(self, LWindow):
        _translate = QtCore.QCoreApplication.translate
        LWindow.setWindowTitle(_translate("LWindow", "LeaderBoard"))
        self.updateBttn.setText(_translate("LWindow", "Update"))
        item = self.leaderboardDisplay.horizontalHeaderItem(0)
        item.setText(_translate("LWindow", "Username"))
        item = self.leaderboardDisplay.horizontalHeaderItem(1)
        item.setText(_translate("LWindow", "Model_Name"))
        item = self.leaderboardDisplay.horizontalHeaderItem(2)
        item.setText(_translate("LWindow", "Model Accuracy"))
        item = self.leaderboardDisplay.horizontalHeaderItem(3)
        item.setText(_translate("LWindow", "Attack %"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LWindow = QtWidgets.QMainWindow()
    ui = Ui_LWindow()
    ui.setupUi(LWindow)
    LWindow.show()
    sys.exit(app.exec_())
