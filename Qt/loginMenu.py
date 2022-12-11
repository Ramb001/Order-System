from PyQt5.QtWidgets import QComboBox, QMainWindow, QApplication, QLineEdit, QWidget, QGridLayout, QPushButton

from Qt.createMenu import CreateWindow
from Actions.checkStaff import checkPerson


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.centralwidget = QWidget()
        self.gridLayout = QGridLayout()
        self.setWindowTitle("WORLD inc.")

        self.lineEditLogin = QLineEdit()
        self.lineEditLogin.setPlaceholderText("Login")
        
        self.lineEditPassword = QLineEdit()
        self.lineEditPassword.setPlaceholderText("Password")

        self.enterToSys = QPushButton()
        self.enterToSys.setText("Enter")
        self.enterToSys.clicked.connect(self.enterSystem)
        
        self.createEmployee = QPushButton()
        self.createEmployee.setText("Create")
        self.createEmployee.clicked.connect(self.create)

        self.combobox = QComboBox()
        self.combobox.addItems(['Director', 'Administrator', 'Waiter'])
        
        self.gridLayout.addWidget(self.combobox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.lineEditLogin, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.lineEditPassword, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.enterToSys, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.createEmployee, 2, 1, 1, 1)
        
        self.centralwidget.setLayout(self.gridLayout)
        self.setCentralWidget(self.centralwidget)
        
    def create(self):
        self.createWindow = CreateWindow()
        self.createWindow.show()
        
    def enterSystem(self):
        post = str(self.combobox.currentText()).lower()
        login = str(self.lineEditLogin.text())
        password =  str(self.lineEditPassword.text())
        if len(login) != 0 and len(password) != 0:
            if checkPerson(post, login, password):
                self.enterToSys.setStyleSheet("color : green")
                login = ''
                password = ''
            else:
                self.enterToSys.setStyleSheet("color : red")
        else:
            self.enterToSys.setStyleSheet("color : red")
            

        
def main():
    app = QApplication([""])
    w = LoginWindow()
    w.show()
    app.exec_()