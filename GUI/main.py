import sys
sys.path.insert(0, '/Users/chris/Desktop/CS419MachineLearning/GUI/components')
from PyQt5 import QtWidgets
from client import Ui_CWindow
from signIn import Ui_SIWindow
from signUp import Ui_SUWindow
from Admin import Ui_AGMWindow
from AdminBM import Ui_ABMWindow
from AdminWM import Ui_AWMWindow
from User import Ui_UWindow
from UserBM import Ui_UBMWindow
from UserWM import Ui_UWMWindow
from leaderboard import Ui_LWindow
import clientConnect as C
import login as L

class CWindow(QtWidgets.QMainWindow, Ui_CWindow):
    
    def __init__(self, parent=None):
        super(CWindow, self).__init__(parent)
        self.setupUi(self)
        self.signInButton.clicked.connect(self.hide)
        self.signUpButton.clicked.connect(self.hide)


class SIWindow(QtWidgets.QMainWindow, Ui_SIWindow):
    def __init__(self, parent=None):
        super(SIWindow, self).__init__(parent)
        self.setupUi(self)
        self.backBttn.clicked.connect(self.hide)
        self.signBttn.clicked.connect(self.hide)

class SUWindow(QtWidgets.QMainWindow, Ui_SUWindow):
    def __init__(self, parent=None):
        super(SUWindow, self).__init__(parent)
        self.setupUi(self)
        self.backBttn.clicked.connect(self.hide)
        self.signBttn.clicked.connect(self.hide)

class AGMWindow(QtWidgets.QMainWindow, Ui_AGMWindow):
    def __init__(self, parent=None):
        super(AGMWindow, self).__init__(parent)
        self.setupUi(self)
        self.signOutButton.clicked.connect(self.hide)
        self.updateButton.clicked.connect(self.hide)

class AWMWindow(QtWidgets.QMainWindow, Ui_AWMWindow):
    def __init__(self, parent=None):
        super(AWMWindow, self).__init__(parent)
        self.setupUi(self)
        self.signOutButton.clicked.connect(self.hide)
        self.updateButton.clicked.connect(self.hide)

class ABMWindow(QtWidgets.QMainWindow, Ui_ABMWindow):
    def __init__(self, parent=None):
        super(ABMWindow, self).__init__(parent)
        self.setupUi(self)
        self.signOutButton.clicked.connect(self.hide)
        self.updateButton.clicked.connect(self.hide)

class UWindow(QtWidgets.QMainWindow, Ui_UWindow):
    def __init__(self, parent=None):
        super(UWindow, self).__init__(parent)
        self.setupUi(self)
        self.signOutButton.clicked.connect(self.hide)

class UBMWindow(QtWidgets.QMainWindow, Ui_UBMWindow):
    def __init__(self, parent=None):
        super(UBMWindow, self).__init__(parent)
        self.setupUi(self)
        self.signOutButton.clicked.connect(self.hide)

class UWMWindow(QtWidgets.QMainWindow, Ui_UWMWindow):
    def __init__(self, parent=None):
        super(UWMWindow, self).__init__(parent)
        self.setupUi(self)
        self.signOutButton.clicked.connect(self.hide)
        
class LWindow(QtWidgets.QMainWindow, Ui_LWindow):
    def __init__(self, parent=None):
        super(LWindow, self).__init__(parent)
        self.setupUi(self)


class Manager:
    def __init__(self):
        self.first = CWindow()
        self.second = SIWindow()
        self.third = SUWindow()
        self.fourth = AGMWindow()
        self.fifth = AWMWindow()
        self.sixth = ABMWindow()
        self.seventh = UWindow()
        self.eigth = UWMWindow()
        self.ninth = UBMWindow()
        self.tenth = LWindow()

############All of the button programming for the initial screen#######
        self.first.signInButton.clicked.connect(self.second.show)
        self.first.signUpButton.clicked.connect(self.third.show)
############All of the button programming for the signIn screen########
        self.second.backBttn.clicked.connect(self.first.show)
        self.second.signBttn.clicked.connect(self.loginCheck)
############All of the button programming for the signUp screen########
        self.third.signBttn.clicked.connect(self.loginCheckU)
        self.third.backBttn.clicked.connect(self.first.show)
############All of the button programming for the Admin GM screen######
        self.fourth.signOutButton.clicked.connect(self.second.show)
        self.fourth.updateButton.clicked.connect(self.second.show)
        self.fourth.updateButton.clicked.connect(self.updateModeG)
        self.fourth.dataButton.clicked.connect(self.submitDatasetG)
        self.fourth.modelButton.clicked.connect(self.submitModelG) 
        self.fourth.boardButton.clicked.connect(self.tenth.show)
        self.fourth.constraintsButton.clicked.connect(self.submitConstraints)
############All of the button programming for the Admin WM screen######
        self.fifth.signOutButton.clicked.connect(self.second.show)
        self.fifth.updateButton.clicked.connect(self.second.show)
        self.fifth.updateButton.clicked.connect(self.updateModeW)
        self.fifth.dataButton.clicked.connect(self.submitDatasetW)
        self.fifth.modelButton.clicked.connect(self.submitModelW) 
        self.fifth.boardButton.clicked.connect(self.tenth.show)
############All of the button programming for the Admin BM screen######
        self.sixth.signOutButton.clicked.connect(self.second.show)
        self.sixth.updateButton.clicked.connect(self.second.show)
        self.sixth.updateButton.clicked.connect(self.updateModeB)
        self.sixth.dataButton.clicked.connect(self.submitDatasetB)
        self.sixth.boardButton.clicked.connect(self.tenth.show)
############All of the button programming for the User GM screen######
        self.seventh.signOutButton.clicked.connect(self.second.show)
        self.seventh.boardButton.clicked.connect(self.tenth.show)
        self.seventh.boardButton.clicked.connect(self.getData)
        self.seventh.fileButton.clicked.connect(self.submitImageS)
        self.seventh.algoButton.clicked.connect(self.submitAttackS)
        self.seventh.modelButton.clicked.connect(self.submitModelS)
        self.seventh.dataButton.clicked.connect(self.getDatasetS)
        self.seventh.updateListBttn.clicked.connect(self.updateLists)
############All of the button programming for the User WM screen#######
        self.eigth.signOutButton.clicked.connect(self.second.show)
        self.eigth.boardButton.clicked.connect(self.tenth.show)
        self.eigth.boardButton.clicked.connect(self.getData)
        self.eigth.fileButton.clicked.connect(self.submitImageE)
        self.eigth.modelButton.clicked.connect(self.submitModelE)
        self.eigth.algoButton.clicked.connect(self.submitAttackE)
        self.eigth.dataButton.clicked.connect(self.getDatasetE)
        self.eigth.updateListBttn.clicked.connect(self.updateListsE)
############All of the button programming for the User BM screen#######
        self.ninth.signOutButton.clicked.connect(self.second.show)
        self.ninth.boardButton.clicked.connect(self.getData)
        self.ninth.boardButton.clicked.connect(self.tenth.show)
        self.ninth.updateListBttn.clicked.connect(self.updateLists)
        self.ninth.updateListBttn.clicked.connect(self.updateLists)
        self.ninth.fileButton.clicked.connect(self.submitImageN)
        self.ninth.modelButton.clicked.connect(self.submitModelN)
        self.ninth.dataButton.clicked.connect(self.getDatasetN)
        self.ninth.algoButton.clicked.connect(self.submitAttackN)
        self.ninth.updateListBttn.clicked.connect(self.updateListsN)
###########All of the button programming for Leaderboard screen########
        self.tenth.updateBttn.clicked.connect(self.getData)
#######################################################################
        self.first.show()
#########All THE METHODS USED FOR THE BUTTONS##########################
    def loginCheck(self):
        try:
            user = self.second.userText.toPlainText().strip()
            passw = self.second.passText.toPlainText().strip()
            res = L.login(user,passw)
            if res == "user":
                self.second.userText.clear()
                self.second.passText.clear()
                mode = C.getMode()
                if mode == "Gray":
                   self.loadAttacks()
                   self.loadModels()
                   self.loadImages()
                   self.seventh.userWelcome.setText(user)
                   self.seventh.show()
                elif mode == "White":
                   self.loadModelsE()
                   self.loadAttacksE()
                   self.loadImagesE()
                   self.eigth.userWelcome.setText(user)
                   self.eigth.show()
                elif mode == "Black":
                   self.loadModelsN()
                   self.loadAttacksN()
                   self.loadImagesN()
                   self.ninth.userWelcome.setText(user)
                   self.ninth.show()
            elif res == "admin":
                self.second.userText.clear()
                self.second.passText.clear()
                mode = C.getMode()
                if mode == "Gray":
                    self.fourth.userWelcome.setText(user)
                    self.fourth.show()
                elif mode == "White":
                    self.fifth.userWelcome.setText(user)
                    self.fifth.show()
                elif mode == "Black":
                    self.sixth.userWelcome.setText(user)
                    self.sixth.show()
            else:
                self.second.userText.clear()
                self.second.passText.clear()
                self.second.errorDisplay.setText("ERROR: Your username and/or password aren't in the system!!!")
        except Exception as e:
            print(e)
#################################################################
    def loginCheckU(self):
        user = self.third.userText.toPlainText().strip()
        passw = self.third.passText.toPlainText().strip()
        con = self.third.conText.toPlainText()
        if con == passw:
            res = L.register_DB(user,passw)
            if res == "user":
                self.third.userText.clear()
                self.third.passText.clear()
                mode = C.getMode()
                if mode == "Gray":
                    self.loadAttacks()
                    self.loadModels()
                    self.loadImages()
                    self.seventh.userWelcome.setText(user)
                    self.seventh.show()
                elif mode == "White":
                    self.loadAttacksE()
                    self.loadModelsE()
                    self.loadImagesE()
                    self.eigth.userWelcome.setText(user)
                    self.eigth.show()
                elif mode == "Black":
                    self.loadAttacksN()
                    self.loadModelsN()
                    self.loadImagesN()
                    self.ninth.userWelcome.setText(user)
                    self.ninth.show()
            elif res == "admin":
                self.third.userText.clear()
                self.third.passText.clear()
                mode = C.getMode()
                if mode == "Gray":
                     self.fourth.userWelcome.setText(user)
                     self.fourth.show()
                elif mode == "White":
                    self.fifth.userWelcome.setText(user)
                    self.fifth.show()
                elif mode == "Black":
                    self.sixth.userWelcome.setText(user)
                    self.sixth.show()
            else:
                self.third.userText.clear()
                self.third.passText.clear()
                self.third.conText.clear()
                self.third.errorDisplay.setText("ERROR: Your passwords do not match. Please fix them!!!")
########################################################################
    def updateModeG(self):
        newMode = self.fourth.gamemodes.currentText()
        if newMode == "Gray-Box":
            return
        elif newMode == "White-Box":
            newMode = "White"
        elif newMode == "Black-Box":
            newMode = "Black"
        C.updateMode(newMode)
    def submitModelG(self):
        try:
            sM = self.fourth.modelText.toPlainText().strip()
            sMA = self.fourth.modelTextA.toPlainText().strip()
            if sM != "" and sMA != "":
                sMA = int(sMA)
                C.submitModel(sM, self.fourth.userWelcome.text(),sMA)
        except:
            print("You're missing information")
            
    def submitDatasetG(self):
        try:
            sD = self.fourth.dataText.toPlainText().strip()
            if sD != "":
                res = C.submitDataset(sD)
                if res == True:
                    DDB.registerDataset(self.fourth.userWelcome.text(),sD)
        except:
            print("You're missing information")
    def submitConstraints(self):
        op = self.fourth.outputText.toPlainText().strip()
        freq = self.fourth.frequencyText.toPlainText().strip()
        result = self.fourth.resultText.toPlainText().strip()
        query = self.fourth.queryText.toPlainText().strip()      
        if query == "" and freq != "":
            self.seventh.queryText.setText("N/A")
            self.seventh.frequencyText.setText(freq)
        elif  query != "" and freq == "":
            self.seventh.queryText.setText(query)
            self.seventh.frequencyText.setText("N/A")
        if result == "" and op != "":
            self.seventh.outputText.setText(op)
            self.seventh.resultText.setText("N/A")
        elif  result != "" and op == "":
            self.seventh.outputText.setText("N/A")
            self.seventh.resultText.setText(result)
        else:
            print("you can't fill in both of them for each option")
########################################################################
    def updateModeW(self):
        newMode = self.fifth.gamemodes.currentText()
        if newMode == "Gray-Box":
            newMode = "Gray"
        elif newMode == "White-Box":
            return
        elif newMode == "Black-Box":
            newMode = "Black"
        C.updateMode(newMode)
    
    def submitDatasetW(self):
        try:
            sD = self.fifth.dataText.toPlainText().strip()
            if sD != "":
                res = C.submitDataset(sD)
                if res == True:
                    DDB.registerDataset(self.fifth.userWelcome.text(),sD)
        except:
            print("You're missing information")
    
    def submitModelW(self):
        try:
            sM = self.fifth.modelText.toPlainText().strip()
            sMA = self.fifth.modelTextA.toPlainText().strip()
            if sM != "" and sMA != "":
                sMA = int(sMA)
                C.submitModel(sM, self.fifth.userWelcome.text(),sMA)
        except:
            print("You're missing information")     
########################################################################
    def updateModeB(self):
        newMode = self.sixth.gamemodes.currentText()
        if newMode == "Gray-Box":
            newMode = "Gray"
        elif newMode == "White-Box":
            newMode = "White"
        elif newMode == "Black-Box":
            return
        C.updateMode(newMode)
    
    def submitDatasetB(self):
        try:
            sD = self.sixth.dataText.toPlainText().strip()
            if sD != "":
                res = C.submitDataset(sD)
                if res == True:
                    DDB.registerDataset(self.fifth.userWelcome.text(),sD)
        except:
            print("You're missing information")
                
#################################################################           
    def submitImageS(self):
        try:
            self.seventh.errordisplay.append("Submitting Image....")
            sI = self.seventh.fileName.toPlainText().strip()
            if sI != "":
                C.submitImage(sI, self.seventh.userWelcome.text().strip())
                self.seventh.errordisplay.append("Image Submitted Successfully.")
        except Exception as e:
            self.seventh.errordisplay.append("You're missing information or ", e)
    def submitAttackS(self):
        try:
            self.seventh.errordisplay.append("Submitting Attack....")
            sI = self.seventh.algoText.toPlainText().strip()
            if sI != "":
                C.submitAlgorithm(sI, self.seventh.userWelcome.text().strip())
                self.seventh.errordisplay.append("Algorithm Submitted Successfully.")
        except Exception as e:
            self.seventh.errordisplay.append("You're missing information or ", e)
    def submitModelS(self):
        try:
            self.seventh.errordisplay.append("Submitting Model....")
            sM = self.seventh.modelText.toPlainText().strip()
            sMA = self.seventh.modelTextA.toPlainText().strip()
            if sM != "" and sMA != "":
                sMA = int(sMA)
                C.submitModel(sM, self.userWelcome.text(),sMA)
                self.seventh.errordisplay.append("Model Submitted Successfully.")
        except Exception as e:
            self.seventh.errordisplay.append("You're missing information or ", e)
    def getDatasetS(self):
        try:
            self.seventh.errordisplay.append("Downloading Dataset....")
            dataName = self.eigth.datasetList.currentItem().text()
            if dataName != "":
               C.getDatasets(dataName)
               self.seventh.errordisplay.append("Dataset Downloaded Successfully.")
        except:
            self.seventh.errordisplay.append("Nothing is selected or ", e)
    def loadAttacks(self):
        try:
            attackList = C.getAttacks()
            for x in attackList:
                self.seventh.attackList.addItem(x)
        except Exception as e:
            self.seventh.errordisplay.append(e)
    def loadModels(self):
        try:
            modelList = C.getModels()
            for x in modelList:
                self.seventh.modelList.addItem(x)
        except Exception as e:
            self.seventh.errordisplay.append(e)
    def loadImages(self):
        try:
            imageList = C.getImages()
            for x in imageList:
                self.seventh.imageList.addItem(x)
        except Exception as e:
            self.seventh.errordisplay.append(e)
    def updateLists(self):
        try:
            self.seventh.errordisplay.append("Updating List....")
            self.seventh.attackList.clear()
            self.loadAttacks()
            self.seventh.modelList.clear()
            self.loadModels()
            self.seventh.imageList.clear()
            self.loadImages()
            self.seventh.errordisplay.append("Updated Successfully.")
        except Exception as e:
            self.seventh.errordisplay.append(e)
#################################################################
    def submitImageE(self):
        try:
            self.eigth.errordisplay.append("Submitting Image....")
            sI = self.eigth.fileName.toPlainText().strip()
            if sI != "":
                C.submitImage(sI, self.eigth.userWelcome.text().strip())
                self.eigth.errordisplay.append("Image Submitted Successfully.")
        except Exception as e:
            self.eigth.errordisplay.append("You're missing information or ", e)
    def submitAttackE(self):
        try:
            self.eigth.errordisplay.append("Submitting Attack....")
            sI = self.eigth.algoText.toPlainText().strip()
            if sI != "":
                C.submitAlgorithm(sI, self.eigth.userWelcome.text().strip())
                self.eigth.errordisplay.append("Algorithm Submitted Successfully.")
        except Exception as e:
            self.eigth.errordisplay.append("You're missing information or ", e)
    def submitModelE(self):
        try:
            self.eigth.errordisplay.append("Submitting Model....")
            sM = self.eigth.modelText.toPlainText().strip()
            sMA = self.eigth.modelTextA.toPlainText().strip()
            if sM != "" and sMA != "":
                sMA = int(sMA)
                C.submitModel(sM, self.eigth.userWelcome.text(),sMA)
                self.eigth.errordisplay.append("Model Submitted Successfully.")
        except Exception as e:
            self.eigth.errordisplay.append("You're missing information or ", e)        
    def getDatasetE(self):
        try:
            self.eigth.errordisplay.append("Downloading Dataset....")
            dataName = self.seventh.datasetList.currentItem().text()
            if dataName != "":
               C.getDatasets(dataName)
               self.eigth.errordisplay.append("Dataset Downloaded Successfully.")
        except Exception as e:
            self.eigth.errordisplay.append("Nothing is selected or ", e)
    def loadAttacksE(self):
        try:
            attackList = C.getAttacks()
            for x in attackList:
                self.eigth.attackList.addItem(x)
        except Exception as e:
            self.eigth.errordisplay.append(e)
    def loadModelsE(self):
        try:
            modelList = C.getModels()
            for x in modelList:
                self.eigth.modelList.addItem(x)
        except Exception as e:
            self.eigth.errordisplay.append(e)
    def loadImagesE(self):
        try:
            imageList = C.getImages()
            for x in imageList:
                self.eigth.imageList.addItem(x)
        except Exception as e:
            self.eigth.errordisplay.append(e)
    def updateListsE(self):
        try:
            self.eigth.errordisplay.append("Updating List....")
            self.eigth.attackList.clear()
            self.loadAttacks()
            self.eigth.modelList.clear()
            self.loadModels()
            self.eigth.imageList.clear()
            self.loadImages()
            self.eigth.errordisplay.append("Updated Successfully.")
        except Exception as e:
            self.eigth.errordisplay.append(e)
########################################################################
    def submitImageN(self):
        try:
            self.ninth.errordisplay.append("Submitting Image....")
            sI = self.ninth.fileName.toPlainText().strip()
            if sI != "":
                C.submitImage(sI, self.ninth.userWelcome.text().strip())
                self.ninth.errordisplay.append("Image Submitted Successfully.")
        except Exception as e:
            self.ninth.errordisplay.append("You're missing information or ", e)
    def submitAttackN(self):
        try:
            self.ninth.errordisplay.append("Submitting Attack....")
            sI = self.ninth.algoText.toPlainText().strip()
            if sI != "":
                C.submitAlgorithm(sI, self.ninth.userWelcome.text().strip())
                self.ninth.errordisplay.append("Algorithm Submitted Successfully.")
        except Exception as e:
            self.ninth.errordisplay.append("You're missing information or ", e) 
    def submitModelN(self):
        try:
            self.ninth.errordisplay.append("Submitting Model....")
            sM = self.ninth.modelText.toPlainText().strip()
            sMA = self.ninth.modelTextA.toPlainText().strip()
            if sM != "" and sMA != "":
                sMA = int(sMA)
                C.submitModel(sM, self.ninth.userWelcome.text(),sMA)
                self.ninth.errordisplay.append("Model Submitted Successfully.")
        except Exception as e:
            self.ninth.errordisplay.append("You're missing information or ", e)          
    def getDatasetN(self):
        try:
            self.ninth.errordisplay.append("Downloading Dataset....")
            dataName = self.ninth.datasetList.currentItem().text()
            if dataName != "":
               C.getDatasets(dataName)
               self.ninth.errordisplay.append("Dataset Downloaded Successfully.")
        except Exception as e:
            self.ninth.errordisplay.append("Nothing is selected or ", e)

    def loadAttacksN(self):
        try:
            attackList = C.getAttacks()
            for x in attackList:
                self.ninth.attackList.addItem(x)
        except Exception as e:
            self.ninth.errordisplay.append(e)
    def loadModelsN(self):
        try:
            modelList = C.getModels()
            for x in modelList:
                self.ninth.modelList.addItem(x)
        except Exception as e:
            self.ninth.errordisplay.append(e)
    def loadImagesN(self):
        try:
            imageList = C.getImages()
            for x in imageList:
                self.ninth.imageList.addItem(x)
        except Exception as e:
            self.ninth.errordisplay.append(e)
    def updateListsN(self):
        try:
            self.ninth.errordisplay.append("Updating List....")
            self.ninth.attackList.clear()
            self.loadAttacks()
            self.ninth.modelList.clear()
            self.loadModels()
            self.ninth.imageList.clear()
            self.loadImages()
            self.ninth.errordisplay.append("Updated Successfully.")
        except Exception as e:
            self.ninth.errordisplay.append(e)
########################################################################
    def getData(self):
        table = C.getBoard()
        i = 0
        r = 0
        c = 0
        for x in table:
            if r == 20:
                return
            if (i+1/4) == 1:
                r += 1
                c = 0
                i = 0
            else:
                item = QtWidgets.QTableWidgetItem()
                item.setText(x)
                self.tenth.leaderboardDisplay.setItem(r,c,item)
                i += 1
                c += 1

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())
