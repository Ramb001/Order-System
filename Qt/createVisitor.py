from PyQt5.QtWidgets import QLineEdit, QWidget, QGridLayout, QPushButton, QMainWindow, QApplication

from Actions.createVisitor import add
from Actions.checkVisitors import checkVisitor


class CreateVisitor(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.centralwidget = QWidget()
        self.gridLayout = QGridLayout()
        self.setWindowTitle("Create new visitor")
        
        self.lineEditName = QLineEdit()
        self.lineEditName.setPlaceholderText("Name")

        self.createVisitor = QPushButton()
        self.createVisitor.setText("Create")
        self.createVisitor.clicked.connect(self.addNewUser)
        
        self.gridLayout.addWidget(self.lineEditName, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.createVisitor, 1, 1, 1, 1)
        
        self.centralwidget.setLayout(self.gridLayout)
        self.setCentralWidget(self.centralwidget)
    
    def addNewUser(self):
        name =  str(self.lineEditName.text())
        if not checkVisitor(name):
            if len(name) != 0:
                add(name)
                self.createVisitor.setStyleSheet("color : green")
                name = ''
        else:
            self.createVisitor.setStyleSheet("color : red")