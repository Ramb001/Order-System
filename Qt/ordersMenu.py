from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QVBoxLayout

from Qt.createOrder import CreateOrder


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
        self.orders = []
        
        self.gridLayout.addWidget(self.createOrder, 0, 0, 1, 1)
        
        self.centralwidget.setLayout(self.gridLayout)
        self.setCentralWidget(self.centralwidget)
        
    def createOrders(self):
        self.createMenu = CreateOrder()
        self.createMenu.show()