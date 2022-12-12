from PyQt5.QtWidgets import QLineEdit, QWidget, QGridLayout, QPushButton, QMainWindow, QApplication

from Actions.createVisitor import add


class CreateVisitor(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.centralwidget = QWidget()
        self.gridLayout = QGridLayout()
        self.setWindowTitle("Create new visitor")

        self.lineEditSurname = QLineEdit()
        self.lineEditSurname.setPlaceholderText("Surname")
        
        self.lineEditName = QLineEdit()
        self.lineEditName.setPlaceholderText("Name")
        

        self.createVisitor = QPushButton()
        self.createVisitor.setText("Create")
        self.createVisitor.clicked.connect(self.addNewUser)
        
        self.gridLayout.addWidget(self.lineEditSurname, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.lineEditName, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.createVisitor, 1, 1, 1, 1)
        
        self.centralwidget.setLayout(self.gridLayout)
        self.setCentralWidget(self.centralwidget)
    
    def addNewUser(self):
        surname = str(self.lineEditSurname.text())
        name =  str(self.lineEditName.text())
        if len(surname) != 0 and len(name) != 0:
            add(surname, name)
            self.createVisitor.setStyleSheet("color : green")
            surname = ''
            name = ''
        else:
            self.createVisitor.setStyleSheet("color : red")