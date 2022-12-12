from PyQt5.QtWidgets import QLineEdit, QWidget, QGridLayout, QPushButton, QMainWindow, QComboBox

from Actions.getCategories import getCategories
from Actions.getNames import getNames


class CreateOrder(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.centralwidget = QWidget()
        self.gridLayout = QGridLayout()
        self.setWindowTitle("New order")

        self.createOrder = QPushButton()
        self.createOrder.setText("Create")
        
        self.category = QComboBox()
        self.category.addItems(getCategories())
        self.category.currentIndexChanged.connect(self.updateCombo)
        
        self.position = QComboBox()
        self.position.addItems(['Мартини Амаро'])
        
        self.gridLayout.addWidget(self.category, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.position, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.createOrder, 2, 0, 1, 1)
        
        self.centralwidget.setLayout(self.gridLayout)
        self.setCentralWidget(self.centralwidget)
        
    def updateCombo(self):
        self.position.clear()
        self.position.addItems(getNames(str(self.category.currentText())))