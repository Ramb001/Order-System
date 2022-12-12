from PyQt5.QtWidgets import QLineEdit, QWidget, QGridLayout, QPushButton, QMainWindow, QComboBox

from Actions.getCategories import getCategories
from Actions.getNames import getNames
from Actions.getPersons import getVisitors


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
        
        self.addButton = QPushButton()
        self.addButton.setText("Add")
        
        self.category = QComboBox()
        self.category.addItems(getCategories())
        self.category.currentIndexChanged.connect(self.updateCombo)
        
        self.position = QComboBox()
        self.position.addItems(['Мартини Амаро'])
        
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