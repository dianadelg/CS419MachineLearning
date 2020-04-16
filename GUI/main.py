from PyQt5 import QtWidgets

from client import Ui_CWindow
from signIn import Ui_SIWindow
from signUp import Ui_SUWindow


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

class SUWindow(QtWidgets.QMainWindow, Ui_SUWindow):
    def __init__(self, parent=None):
        super(SUWindow, self).__init__(parent)
        self.setupUi(self)
        self.backBttn.clicked.connect(self.hide)



class Manager:
    def __init__(self):
        self.first = CWindow()
        self.second = SIWindow()
        self.third = SUWindow()
        
        self.first.signInButton.clicked.connect(self.second.show)
        self.first.signUpButton.clicked.connect(self.third.show)
        self.second.backBttn.clicked.connect(self.first.show)
        self.third.backBttn.clicked.connect(self.first.show)
        
        self.first.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())
