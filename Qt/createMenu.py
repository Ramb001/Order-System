from PyQt5.QtWidgets import QLineEdit, QWidget, QGridLayout, QPushButton, QMainWindow, QComboBox

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
        self.combobox.currentIndexChanged.connect(self.currentPost)
        self.createEmployee.clicked.connect(self.currentPost)
        
        self.gridLayout.addWidget(self.combobox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.lineEditLogin, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.lineEditPassword, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.createEmployee, 2, 1, 1, 1)
        
        self.centralwidget.setLayout(self.gridLayout)
        self.setCentralWidget(self.centralwidget)
        
    
    def currentPost(self, index):
        post = self.items[index]
        print(post)