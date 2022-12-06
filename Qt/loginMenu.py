from PyQt5.QtWidgets import QComboBox, QMainWindow, QApplication, QLineEdit, QWidget, QGridLayout, QPushButton

from numpy import maximum

from Qt.createMenu import CreateWindow


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
        
        self.createEmployee = QPushButton()
        self.createEmployee.setText("Create")

        self.combobox = QComboBox()
        self.combobox.addItems(['Director', 'Administrator', 'Waiter'])
        
        self.gridLayout.addWidget(self.combobox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.lineEditLogin, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.lineEditPassword, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.enterToSys, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.createEmployee, 2, 1, 1, 1)
        self.createEmployee.clicked.connect(self.create)
        
        self.centralwidget.setLayout(self.gridLayout)
        self.setCentralWidget(self.centralwidget)
        
    def create(self):
        self.createWindow = CreateWindow()
        self.createWindow.show()
            

        
def main():
    app = QApplication([""])
    w = LoginWindow()
    w.show()
    app.exec_()