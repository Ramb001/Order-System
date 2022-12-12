from PyQt5.QtWidgets import QLineEdit, QWidget, QGridLayout, QPushButton, QMainWindow, QComboBox

from Actions.getCategories import getCategories


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
        
        self.gridLayout.addWidget(self.category, 0, 1, 1, 1)
        
        self.centralwidget.setLayout(self.gridLayout)
        self.setCentralWidget(self.centralwidget)
        