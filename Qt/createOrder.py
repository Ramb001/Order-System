from PyQt5.QtWidgets import QLineEdit, QWidget, QGridLayout, QPushButton, QMainWindow, QComboBox
from sqlalchemy import table

from Actions.getCategories import getCategories
from Actions.getNames import getNames
from Actions.getPersons import getVisitors
from Actions.stackOrder import stack, add


class CreateOrder(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.centralwidget = QWidget()
        self.gridLayout = QGridLayout()
        self.setWindowTitle("New order")
        
        self.choosePerson = QComboBox()
        self.choosePerson.addItems(getVisitors())

        self.createOrder = QPushButton()
        self.createOrder.setText("Create")
        self.createOrder.clicked.connect(self.createOrd)
        
        self.addButton = QPushButton()
        self.addButton.setText("Add")
        self.addButton.clicked.connect(self.getOrder)
        
        self.category = QComboBox()
        self.category.addItems(getCategories())
        self.category.currentIndexChanged.connect(self.updateCombo)
        
        self.position = QComboBox()
        self.position.addItems(['Мартини спирито'])
        
        self.amount = QLineEdit()
        self.amount.setPlaceholderText("Amount")
        
        self.table = QLineEdit()
        self.table.setPlaceholderText("Number of table")
        
        self.gridLayout.addWidget(self.table, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.choosePerson, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.category, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.position, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.amount, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.addButton, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.createOrder, 6, 0, 1, 1)
        
        self.centralwidget.setLayout(self.gridLayout)
        self.setCentralWidget(self.centralwidget)
        
    def updateCombo(self):
        self.position.clear()
        self.position.addItems(getNames(str(self.category.currentText())))
        
    def getOrder(self):
        tableNum = str(self.table.text())
        category = str(self.category.currentText())
        visitor = str(self.choosePerson.currentText())
        position = str(self.position.currentText())
        amount = str(self.amount.text())
        if len(amount) != 0 and len(tableNum) != 0 and len(visitor) != 0:
            stack(tableNum, visitor, category, position, amount)
            self.addButton.setStyleSheet("color : green")
        else:
            self.addButton.setStyleSheet("color : red")
            
    def createOrd(self):
        add()
        self.createOrder.setStyleSheet("color : green")