from PyQt5.QtWidgets import QLineEdit, QWidget, QGridLayout, QPushButton, QMainWindow


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
        
        self.lineEditPost = QLineEdit()
        self.lineEditPost.setPlaceholderText("Post")

        self.createEmployee = QPushButton()
        self.createEmployee.setText("Create")
        
        self.gridLayout.addWidget(self.lineEditPost, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.lineEditLogin, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.lineEditPassword, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.createEmployee, 2, 1, 1, 1)
        
        self.centralwidget.setLayout(self.gridLayout)
        self.setCentralWidget(self.centralwidget)