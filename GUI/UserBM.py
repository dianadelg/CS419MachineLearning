from PyQt5 import QtWidgets, QtCore, QtGui
import datasetDB as DDB

class Ui_UBMWindow(object):
    def loadDatasets(self):
        try:
            dataList = DDB.getDatasets()
            for x in dataList:
                self.datasetList.addItem(x[0])
        except Exception as e:
            print(e)
            
    def setupUi(self, UBMWindow):
        UBMWindow.setObjectName("UBMWindow")
        UBMWindow.resize(1900, 1400)
        self.centralwidget = QtWidgets.QWidget(UBMWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.userWelcome = QtWidgets.QLineEdit(self.centralwidget)
        self.userWelcome.setEnabled(False)
        self.userWelcome.setGeometry(QtCore.QRect(0, 0, 400, 50))
        self.userWelcome.setObjectName("userWelcome")
        self.boardButton = QtWidgets.QPushButton(self.centralwidget)
        self.boardButton.setGeometry(QtCore.QRect(1650, 70, 200, 70))
        self.boardButton.setObjectName("boardButton")
        self.signOutButton = QtWidgets.QPushButton(self.centralwidget)
        self.signOutButton.setGeometry(QtCore.QRect(1650, 0, 200, 60))
        self.signOutButton.setObjectName("signOutButton")
        self.fileButton = QtWidgets.QPushButton(self.centralwidget)
        self.fileButton.setGeometry(QtCore.QRect(0, 100, 350, 60))
        self.fileButton.setObjectName("fileButton")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(400, 55, 200, 40))
        self.imageLabel.setObjectName("imageName")
        self.fileName = QtWidgets.QTextEdit(self.centralwidget)
        self.fileName.setGeometry(QtCore.QRect(400, 100, 395, 60))
        self.fileName.setObjectName("fileName")
        self.modelButton = QtWidgets.QPushButton(self.centralwidget)
        self.modelButton.setGeometry(QtCore.QRect(0, 220, 350, 60))
        self.modelButton.setObjectName("modelButton")
        self.modelLabel = QtWidgets.QLabel(self.centralwidget)
        self.modelLabel.setGeometry(QtCore.QRect(400, 180, 200, 40))
        self.modelLabel.setObjectName("modelName")
        self.modelText = QtWidgets.QTextEdit(self.centralwidget)
        self.modelText.setGeometry(QtCore.QRect(400, 220, 400, 60))
        self.modelText.setObjectName("modelName")
        self.modelALabel = QtWidgets.QLabel(self.centralwidget)
        self.modelALabel.setGeometry(QtCore.QRect(850, 180, 200, 40))
        self.modelALabel.setObjectName("Accuracy")
        self.modelTextA = QtWidgets.QTextEdit(self.centralwidget)
        self.modelTextA.setGeometry(QtCore.QRect(850, 220, 100, 60))
        self.modelTextA.setObjectName("modelAccuracy")
        self.imageListLabel = QtWidgets.QLabel(self.centralwidget)#FOR THE IMAGELIST LABEL
        self.imageListLabel.setGeometry(QtCore.QRect(600, 440, 150, 30))
        self.imageListLabel.setObjectName("imageListLabel")#FOR THE IMAGELIST
        self.imageList = QtWidgets.QListWidget(self.centralwidget)
        self.imageList.setGeometry(QtCore.QRect(600, 475, 300, 600))
        self.imageList.setObjectName("imageList")
        self.modelListLabel = QtWidgets.QLabel(self.centralwidget)#FOR THE MODELLIST LABEL
        self.modelListLabel.setGeometry(QtCore.QRect(925, 440, 150, 30))
        self.modelListLabel.setObjectName("modelListLabel")
        self.modelList = QtWidgets.QListWidget(self.centralwidget)#FOR THE MODELLIST
        self.modelList.setGeometry(QtCore.QRect(925, 475, 300, 600))
        self.modelList.setObjectName("modelList")
        self.attackListLabel = QtWidgets.QLabel(self.centralwidget)#FOR THE ATTACKLISTLABEL
        self.attackListLabel.setGeometry(QtCore.QRect(1250, 440, 150, 30))
        self.attackListLabel.setObjectName("attackListLabel")
        self.attackList = QtWidgets.QListWidget(self.centralwidget)#FOR THE ATTACKLIST
        self.attackList.setGeometry(QtCore.QRect(1250, 475, 300, 600))
        self.attackList.setObjectName("attackList")
        self.dataListLabel = QtWidgets.QLabel(self.centralwidget)#FOR THE DATALIST LABEL
        self.dataListLabel.setGeometry(QtCore.QRect(20, 440, 150, 30))
        self.dataListLabel.setObjectName("dataListLabel")
        self.datasetList = QtWidgets.QListWidget(self.centralwidget)#FOR THE DATALIST
        self.datasetList.setGeometry(QtCore.QRect(20, 475, 300, 600))
        self.datasetList.setObjectName("datasetList")
        self.dataButton = QtWidgets.QPushButton(self.centralwidget)#FOR THE DATALIST DOWNLOAD BUTTON
        self.dataButton.setGeometry(QtCore.QRect(350, 550, 230, 60))
        self.dataButton.setObjectName("dataButton")
        self.algoButton = QtWidgets.QPushButton(self.centralwidget)#FOR THE ALGORITHM SUBMISSION BUTTON
        self.algoButton.setGeometry(QtCore.QRect(1000, 220, 350, 60))
        self.algoButton.setObjectName("algoButton")
        self.algoLabel = QtWidgets.QLabel(self.centralwidget)#FOR THE ALGORITHM LABEL
        self.algoLabel.setGeometry(QtCore.QRect(1400, 180, 240, 40))
        self.algoLabel.setObjectName("algoLabel")
        self.algoText = QtWidgets.QTextEdit(self.centralwidget)#FOR THE ALGORITHM TEXTBOX
        self.algoText.setGeometry(QtCore.QRect(1400, 220, 400, 60))
        self.algoText.setObjectName("algoName")
        self.loadDatasets()
        self.attackBttn = QtWidgets.QPushButton(self.centralwidget)#FOR THE ATTACK BUTTON
        self.attackBttn.setGeometry(QtCore.QRect(1600, 750, 200, 60))
        self.attackBttn.setObjectName("attackButton")
        self.updateListBttn = QtWidgets.QPushButton(self.centralwidget)#FOR THE UPDATELIST BUTTON
        self.updateListBttn.setGeometry(QtCore.QRect(350, 750, 230, 60))
        self.updateListBttn.setObjectName("updateListButton")
        self.attackInfoLabel = QtWidgets.QLabel(self.centralwidget)#FOR THE ATTACK INFORMATION
        self.attackInfoLabel.setGeometry(QtCore.QRect(600, 410, 1220, 30))
        self.attackInfoLabel.setObjectName("attackInfoLabel")
        self.errorDisplay = QtWidgets.QTextEdit(self.centralwidget)
        self.errorDisplay.setGeometry(QtCore.QRect(0, 1200, 1900, 200))
        self.errorDisplay.setReadOnly(True)
        self.errorDisplay.setObjectName("errorDisplay")
        UBMWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UBMWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 448, 22))
        self.menubar.setObjectName("menubar")
        UBMWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UBMWindow)
        self.statusbar.setObjectName("statusbar")
        UBMWindow.setStatusBar(self.statusbar)
        self.retranslateUi(UBMWindow)
        QtCore.QMetaObject.connectSlotsByName(UBMWindow)

    def retranslateUi(self, UBMWindow):
        _translate = QtCore.QCoreApplication.translate
        UBMWindow.setWindowTitle(_translate("UBMWindow", "User(Black-Box Mode)"))
        self.imageLabel.setText(_translate("UBMWindow", "Image Name"))
        self.signOutButton.setText(_translate("UBMWindow", "Sign Out"))
        self.boardButton.setText(_translate("UBMWindow", "Leaderboard"))
        self.fileButton.setText(_translate("UBMWindow", "Submit an image"))
        self.modelButton.setText(_translate("UBMWindow", "Submit a model"))
        self.dataButton.setText(_translate("UBMWindow", "get Dataset"))
        self.modelLabel.setText(_translate("UBMWindow", "Model Name"))
        self.modelALabel.setText(_translate("UBMWindow", "Accuracy"))
        self.algoButton.setText(_translate("UBMWindow", "Submit an algorithm"))
        self.algoLabel.setText(_translate("UBMWindow", "Algorithm FileName"))
        self.dataButton.setText(_translate("UBMWindow", "Download Dataset"))        
        self.updateListBttn.setText(_translate("UBMWindow", "Update Lists"))
        self.attackBttn.setText(_translate("UBMWindow", "Attack"))
        self.modelListLabel.setText(_translate("UBMWindow", "Model List"))
        self.imageListLabel.setText(_translate("UBMWindow", "Image List"))
        self.attackListLabel.setText(_translate("UBMWindow", "Attack List"))
        self.attackInfoLabel.setText(_translate("UBMWindow", "Please Choose and Image, user submitted model, and an attack algorithm in order to make an attack."))
        self.dataListLabel.setText(_translate("UBMWindow", "Data List"))
        self.errorDisplay.setHtml(_translate("SUWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\"></span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UBMWindow = QtWidgets.QMainWindow()
    ui = Ui_UBMWindow()
    ui.setupUi(UBMWindow)
    UBMWindow.show()
    sys.exit(app.exec_())
