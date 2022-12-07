from PyQt5.QtWidgets import QLineEdit, QWidget, QGridLayout, QPushButton, QMainWindow, QComboBox
from sqlalchemy import false

from Actions.addStaff import add


class CreateWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.centralwidget = QWidget()
        self.gridLayout = QGridLayout()
        self.setWindowTitle("Create new employee")

        self.lineEditLogin = QLineEdit()
        self.lineEditLogin.setPlaceholderText("Login")
        
        self.lineEditPassword = QLineEdit()
        self.lineEditPassword.setPlaceholderText("Password")
        
        self.combobox = QComboBox()
        self.combobox.addItems(['Director', 'Administrator', 'Waiter'])
        self.items = [self.combobox.itemText(i) for i in range(self.combobox.count())]

        self.createEmployee = QPushButton()
        self.createEmployee.setText("Create")
        self.combobox.currentIndexChanged.connect(self.addNewUser)
        self.createEmployee.clicked.connect(self.addNewUser)
        
        self.gridLayout.addWidget(self.combobox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.lineEditLogin, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.lineEditPassword, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.createEmployee, 2, 1, 1, 1)
        
        self.centralwidget.setLayout(self.gridLayout)
        self.setCentralWidget(self.centralwidget)
    
    def addNewUser(self):
        post = str(self.combobox.currentText()).lower()
        login = str(self.lineEditLogin.text())
        password =  str(self.lineEditPassword.text())
        if len(login) != 0 and len(password) != 0:
            add(post, login, password)
            self.createEmployee.setStyleSheet("color : green")
            login = ''
            password = ''
        else:
            self.createEmployee.setStyleSheet("color : red")