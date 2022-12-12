from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QVBoxLayout, QTextBrowser, QLineEdit

from Qt.createOrder import CreateOrder
from Actions.stackOrder import orders


class OrdersMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.centralwidget = QWidget()
        self.gridLayout = QGridLayout()
        self.setWindowTitle("Orders")
        
        self.createOrder = QPushButton()
        self.createOrder.setText("New order")
        self.createOrder.clicked.connect(self.createOrders)
        
        self.orderBox = QVBoxLayout()
        self.orders = list(orders)
        
        self.showOrders = QTextBrowser()
        self.showText()
        
        self.deleteOrder = QLineEdit()
        self.deleteOrder.setPlaceholderText("Number of order")
        
        self.deleteButton = QPushButton()
        self.deleteButton.setText("Delete")
        self.deleteButton.clicked.connect(self.deleteOrders)
        
        self.gridLayout.addWidget(self.showOrders, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.createOrder, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.deleteOrder, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.deleteButton, 3, 0, 1, 1)
        
        self.centralwidget.setLayout(self.gridLayout)
        self.setCentralWidget(self.centralwidget)
        
    def createOrders(self):
        self.createMenu = CreateOrder()
        self.createMenu.show()
        
    def showText(self):
        for i in range(len(self.orders)):
            text = str(f'<b>№{i+1} | Table: {self.orders[i][0]} | Visitor: {self.orders[i][1]}</b>\n')
            self.showOrders.append(text)
        self.showOrders.show()
        
    def deleteOrders(self):
        index = int(self.deleteOrder.text()) - 1
        orders.pop(index)
        self.orders.pop(index)
        self.deleteButton.setStyleSheet("color : green")