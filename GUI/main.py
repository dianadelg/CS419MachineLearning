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
        self.seventh.modelButton.clicked.connect(self.submitModelS)
        self.seventh.dataButton.clicked.connect(self.getDatasetS)
############All of the button programming for the User WM screen#######
        self.eigth.signOutButton.clicked.connect(self.second.show)
        self.eigth.boardButton.clicked.connect(self.tenth.show)
        self.eigth.boardButton.clicked.connect(self.getData)
        self.eigth.fileButton.clicked.connect(self.submitImageE)
        self.eigth.modelButton.clicked.connect(self.submitModelE)
        self.eigth.dataButton.clicked.connect(self.getDatasetE)
############All of the button programming for the User BM screen#######
        self.ninth.signOutButton.clicked.connect(self.second.show)
        self.ninth.boardButton.clicked.connect(self.getData)
        self.ninth.boardButton.clicked.connect(self.tenth.show)
        self.ninth.fileButton.clicked.connect(self.submitImageN)
        self.ninth.modelButton.clicked.connect(self.submitModelN)
        self.ninth.dataButton.clicked.connect(self.getDatasetN)
###########All of the button programming for Leaderboard screen########
        self.tenth.updateBttn.clicked.connect(self.getData)
#######################################################################
        self.first.show()
#########All THE METHODS USED FOR THE BUTTONS##########################
    def loginCheck(self):
        user = self.second.userText.toPlainText()
        passw = self.second.passText.toPlainText()
        res = L.login(user,passw)
        if res == "user":
            self.second.userText.clear()
            self.second.passText.clear()
            mode = C.getMode()
            if mode == "Gray":
               self.seventh.userWelcome.setText(user)
               self.seventh.show()
            elif mode == "White":
               self.eigth.userWelcome.setText(user)
               self.eigth.show()
            elif mode == "Black":
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
#################################################################
    def loginCheckU(self):
        user = self.third.userText.toPlainText()
        passw = self.third.passText.toPlainText()
        con = self.third.conText.toPlainText()
        if con == passw:
            res = L.register_DB(user,passw)
            if res == "user":
                self.third.userText.clear()
                self.third.passText.clear()
                mode = C.getMode()
                if mode == "Gray":
                    self.seventh.userWelcome.setText(user)
                    self.seventh.show()
                elif mode == "White":
                    self.eigth.userWelcome.setText(user)
                    self.eigth.show()
                elif mode == "Black":
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
#################################################################           
    def submitImageS(self):
        try:
            sI = self.seventh.fileName.toPlainText().strip()
            if sI != "":
                C.submitImage(sI, self.seventh.userWelcome.text().strip())
        except Exception as e:
            print("You're missing information or ", e)
    def submitModelS(self):
        try:
            sM = self.seventh.modelText.toPlainText().strip()
            sMA = self.seventh.modelTextA.toPlainText().strip()
            if sM != "" and sMA != "":
                sMA = int(sMA)
                C.submitModel(sM, self.userWelcome.text(),sMA)
        except:
            print("You're missing information")
    def getDatasetS(self):
        try:
            dataName = self.eigth.datasetList.currentItem().text()
            if dataName != "":
               C.getDataset(dataName) 
        except:
            print("Nothing is selected")
#################################################################
    def submitImageE(self):
        try:
            sI = self.eigth.fileName.toPlainText().strip()
            if sI != "":
                C.submitImage(sI, self.eigth.userWelcome.text().strip())
        except Exception as e:
            print("You're missing information or ", e)
    def submitModelE(self):
        try:
            sM = self.eigth.modelText.toPlainText().strip()
            sMA = self.eigth.modelTextA.toPlainText().strip()
            if sM != "" and sMA != "":
                sMA = int(sMA)
                C.submitModel(sM, self.eigth.userWelcome.text(),sMA)
        except:
            print("You're missing information")         
    def getDatasetE(self):
        try:
            dataName = self.seventh.datasetList.currentItem().text()
            if dataName != "":
               C.getDataset(dataName) 
        except:
            print("Nothing is selected")
########################################################################
    def submitImageN(self):
        try:
            sI = self.ninth.fileName.toPlainText().strip()
            if sI != "":
                C.submitImage(sI, self.ninth.userWelcome.text().strip())
        except Exception as e:
            print("You're missing information or ", e)
    def submitModelN(self):
        try:
            sM = self.ninth.modelText.toPlainText().strip()
            sMA = self.ninth.modelTextA.toPlainText().strip()
            if sM != "" and sMA != "":
                sMA = int(sMA)
                C.submitModel(sM, self.ninth.userWelcome.text(),sMA)
        except:
            print("You're missing information")         
    def getDatasetN(self):
        try:
            dataName = self.ninth.datasetList.currentItem().text()
            if dataName != "":
               C.getDataset(dataName) 
        except:
            print("Nothing is selected")
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
                
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())
