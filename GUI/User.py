import datasetDB as DDB
from PyQt5 import QtWidgets, QtCore, QtGui


class Ui_UWindow(object):          
    def loadDatasets(self):
        try:
            dataList = DDB.getDatasets()
            for x in dataList:
                self.datasetList.addItem(x[0])
        except Exception as e:
            print(e)
    def loadImages(self):
        try:
            dataList = DDB.getDatasets()
            for x in dataList:
                self.imageList.addItem(x[0])
        except Exception as e:
            print(e)
    def loadModels(self):
        try:
            dataList = DDB.getDatasets()
            for x in dataList:
                self.modelList.addItem(x[0])
        except Exception as e:
            print(e)
    def setupUi(self, UWindow):
        UWindow.setObjectName("UWindow")
        UWindow.resize(1900, 1400)
        self.centralwidget = QtWidgets.QWidget(UWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.userWelcome = QtWidgets.QLineEdit(self.centralwidget)# FOR THE USERNAME DISPLAY
        self.userWelcome.setEnabled(False)
        self.userWelcome.setGeometry(QtCore.QRect(0, 0, 400, 50))
        self.userWelcome.setObjectName("userWelcome")
        self.boardButton = QtWidgets.QPushButton(self.centralwidget)#FOR THE LEADERBOARD BUTTON
        self.boardButton.setGeometry(QtCore.QRect(1650, 70, 200, 70))
        self.boardButton.setObjectName("boardButton")
        self.signOutButton = QtWidgets.QPushButton(self.centralwidget)#FOR THE SIGN OUT BUTTON
        self.signOutButton.setGeometry(QtCore.QRect(1650, 0, 200, 60))
        self.signOutButton.setObjectName("signOutButton")
        self.fileButton = QtWidgets.QPushButton(self.centralwidget)#FOR THE IMAGE SUBMISSION BUTTON
        self.fileButton.setGeometry(QtCore.QRect(0, 100, 350, 60))
        self.fileButton.setObjectName("fileButton")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)#FOR THE IMAGE LABEL
        self.imageLabel.setGeometry(QtCore.QRect(400, 55, 200, 40))
        self.imageLabel.setObjectName("imageName")
        self.fileName = QtWidgets.QTextEdit(self.centralwidget)#FOR THE IMAGE TEXTBOX
        self.fileName.setGeometry(QtCore.QRect(400, 100, 395, 60))
        self.fileName.setObjectName("fileName")
        self.modelButton = QtWidgets.QPushButton(self.centralwidget)#FOR THE MODEL SUBMISSION BUTTON
        self.modelButton.setGeometry(QtCore.QRect(0, 220, 350, 60))
        self.modelButton.setObjectName("modelButton")
        self.modelLabel = QtWidgets.QLabel(self.centralwidget)#FOR THE MODEL LABEL
        self.modelLabel.setGeometry(QtCore.QRect(400, 180, 200, 40))
        self.modelLabel.setObjectName("modelName")
        self.modelText = QtWidgets.QTextEdit(self.centralwidget)#FOR THE MODEL TEXTBOX
        self.modelText.setGeometry(QtCore.QRect(400, 220, 400, 60))
        self.modelText.setObjectName("modelName")
        self.modelALabel = QtWidgets.QLabel(self.centralwidget)#FOR THE MODEL ACCURACY LABEL
        self.modelALabel.setGeometry(QtCore.QRect(850, 180, 200, 40))
        self.modelALabel.setObjectName("Accuracy")
        self.modelTextA = QtWidgets.QTextEdit(self.centralwidget)#FOR THE MODEL ACCURACY TEXTBOX
        self.modelTextA.setGeometry(QtCore.QRect(850, 220, 100, 60))
        self.modelTextA.setObjectName("modelAccuracy")
        self.queryLabel = QtWidgets.QLabel(self.centralwidget)#FOR THE QUERY CONSTRAINT LABEL
        self.queryLabel.setGeometry(QtCore.QRect(0, 300, 100, 30))
        self.queryLabel.setObjectName("queryLabel")
        self.queryText = QtWidgets.QTextEdit(self.centralwidget)#FOR THE QUERY TEXTBOX
        self.queryText.setGeometry(QtCore.QRect(0, 340, 150, 60))
        self.queryText.setObjectName("queryName")
        self.queryText.setEnabled(False)
        self.frequencyLabel = QtWidgets.QLabel(self.centralwidget)#FOR THE FREQUENCY CONSTRAINT LABEL
        self.frequencyLabel.setGeometry(QtCore.QRect(200, 300, 150, 30))
        self.frequencyLabel.setObjectName("frequencyLabel")
        self.frequencyText = QtWidgets.QTextEdit(self.centralwidget)#FOR THE FREQUENCY TEXTBOX
        self.frequencyText.setGeometry(QtCore.QRect(200, 340, 150, 60))
        self.frequencyText.setObjectName("frequencyName")
        self.frequencyText.setEnabled(False)
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)#FOR THE OUTPUT CONSTRAINT LABEL
        self.outputLabel.setGeometry(QtCore.QRect(600, 300, 100, 30))
        self.outputLabel.setObjectName("outputLabel")
        self.outputText = QtWidgets.QTextEdit(self.centralwidget)#FOR THE OUTPUT TEXTBOX
        self.outputText.setGeometry(QtCore.QRect(600, 340, 150, 60))
        self.outputText.setObjectName("outputName")
        self.outputText.setEnabled(False)
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)#FOR THE RESULT CONSTRIANT LABEL
        self.resultLabel.setGeometry(QtCore.QRect(400, 300, 150, 30))
        self.resultLabel.setObjectName("resultLabel")
        self.resultText = QtWidgets.QTextEdit(self.centralwidget)#FOR THE RESULT TEXTBOX
        self.resultText.setGeometry(QtCore.QRect(400, 340, 150, 60))
        self.resultText.setObjectName("resultName")
        self.resultText.setEnabled(False)
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
        UWindow.setWindowTitle(_translate("UWindow", "User(Gray-Box Mode)"))
        self.signOutButton.setText(_translate("UWindow", "Sign Out"))
        self.boardButton.setText(_translate("UWindow", "Leaderboard"))
        self.imageLabel.setText(_translate("UWindow", "Image FileName"))
        self.fileButton.setText(_translate("UWindow", "Submit an image"))
        self.modelButton.setText(_translate("UWindow", "Submit a model"))
        self.modelLabel.setText(_translate("UWindow", "Model FileName"))
        self.modelALabel.setText(_translate("UWindow", "Accuracy"))
        self.algoButton.setText(_translate("UWindow", "Submit an algorithm"))
        self.algoLabel.setText(_translate("UWindow", "Algorithm FileName"))
        self.frequencyLabel.setText(_translate("UWindow", "Frequency"))
        self.outputLabel.setText(_translate("UWindow", "Output"))
        self.resultLabel.setText(_translate("UWindow", "Result"))
        self.queryLabel.setText(_translate("UWindow", "Query"))
        self.dataButton.setText(_translate("UWindow", "Download Dataset"))        
        self.updateListBttn.setText(_translate("UWindow", "Update Lists"))
        self.attackBttn.setText(_translate("UWindow", "Attack"))
        self.modelListLabel.setText(_translate("UWindow", "Model List"))
        self.imageListLabel.setText(_translate("UWindow", "Image List"))
        self.attackListLabel.setText(_translate("UWindow", "Attack List"))
        self.attackInfoLabel.setText(_translate("UWindow", "Please Choose and Image, user submitted model, and an attack algorithm in order to make an attack."))
        self.dataListLabel.setText(_translate("UWindow", "Data List"))
        self.errorDisplay.setHtml(_translate("SUWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\"></span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UWindow = QtWidgets.QMainWindow()
    ui = Ui_UWindow()
    ui.setupUi(UWindow)
    UWindow.show()
    sys.exit(app.exec_())
